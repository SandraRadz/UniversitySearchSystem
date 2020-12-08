import os
import re

from django.conf import settings
from pyexcel import get_sheet

from universities.models import Country, StudyProgram, StudyProgramInUniversity, University


def import_data():
    uni_data = []
    sheet = get_sheet(
        file_name=os.path.join(settings.BASE_DIR, 'universities.csv'),
        name_columns_by_row=0
    )
    for (
            name, country, program,
            degree_str, price_str, edu_start,
            scholarship, duration, edu_form_str,
            program_description
    ) in zip(
        sheet.column['НАЗВА'],
        sheet.column['КРАЇНА'],
        sheet.column['Програма'],
        sheet.column['Ступінь'],
        sheet.column['Ціна'],
        sheet.column['Початок навчання'],
        sheet.column['Стипендії'],
        sheet.column['Тривалість'],
        sheet.column['Форма навчання'],
        sheet.column['Опис прог'],
    ):
        country_list = Country.objects.filter(name__exact=country)
        if country_list:
            country_obj = country_list.first()
        else:
            country_obj = Country.objects.create(name=country)

        university_list = University.objects.filter(name=name, country=country_obj)
        if university_list:
            university_obj = university_list.first()
        else:
            university_obj = University.objects.create(name=name, country=country_obj)

        study_program_list = StudyProgram.objects.filter(name=program)
        if study_program_list:
            study_program_obj = study_program_list.first()
        else:
            study_program_obj = StudyProgram.objects.create(name=program)

        price_list = re.findall(r'\d+', price_str)
        if price_list:
            price = price_list[0]
        else:
            price = None
        currency = price_str[0]

        if degree_str == "Магістратура":
            degree = StudyProgramInUniversity.master
        else:
            degree = StudyProgramInUniversity.bachelor

        if edu_form_str == "Денна":
            edu_form = StudyProgramInUniversity.offline
        else:
            edu_form = StudyProgramInUniversity.online

        if not scholarship.strip() or scholarship.strip() == "?":
            scholarship_availability = False
            scholarship_description = None
        else:
            scholarship_availability = True
            scholarship_description = scholarship

        uni_data.append(StudyProgramInUniversity(
            study_program=study_program_obj,
            university=university_obj,
            price=price,
            currency=currency,
            scholarship_availability=scholarship_availability,
            scholarship_description=scholarship_description,
            description=program_description,
            duration=duration,
            form_of_study=edu_form,
            degree=degree,
            start_of_study=edu_start)
        )

    StudyProgramInUniversity.objects.bulk_create(uni_data)
