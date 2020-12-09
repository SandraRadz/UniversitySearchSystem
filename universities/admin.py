from django.contrib import admin

# Register your models here.
from universities.models import Country, StudyProgram, University, StudyProgramInUniversity, Grant

admin.site.register(Country)
admin.site.register(StudyProgram)
admin.site.register(University)
admin.site.register(StudyProgramInUniversity)
admin.site.register(Grant)