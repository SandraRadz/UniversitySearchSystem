import os

from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from pyexcel import get_sheet


class Country(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return self.name


class StudyProgram(models.Model):
    FORM_OF_STUDY = (
        ('OFFLINE', 'Offline'),
        ('ONLINE', 'Online')
    )

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    scholarship_availability = models.BooleanField(default=False)
    scholarship_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    duration_in_month = models.IntegerField(null=True, blank=True)
    form_of_study = models.CharField(max_length=10, choices=FORM_OF_STUDY, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(StudyProgram, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    study_programs = models.ManyToManyField(StudyProgram, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(University, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return self.name

    @classmethod
    def populate(cls):
        cls.objects.all().delete()
        uni_data = []
        sheet = get_sheet(
            file_name=os.path.join(settings.BASE_DIR, 'universities.csv'),
            name_columns_by_row=0
        )
        for (
                name, country, program,
                degree, price, edu_start,
                scholarship, duration, edu_form,
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
            country_obj = Country.objects.filter(name__exact=country)
            if len(country_obj) > 0:
                country = country_obj[0]
            else:
                country = Country(name=country).save()
            uni_data.append({
                'name': name,
                'country': country,
                'program': program,
                'degree': degree,
                'price': price,
                'edu_start': edu_start,
                'scholarship': scholarship,
                'duration': duration,
                'edu_form': edu_form,
                'program_description': program_description
            })
        # TODO
        # cls.objects.bulk_create([
        #     cls(
        #         name=data['name'],
        #         description=data['description'],
        #         speaker=data['speaker'],
        #         url=data['url'],
        #         number_of_views=data['number_of_views'],
        #         transcript=data['transcript'],
        #     )
        #     for data in uni_data
        # ])
