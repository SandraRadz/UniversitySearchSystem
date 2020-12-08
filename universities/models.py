import os

from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from pyexcel import get_sheet


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    @property
    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class StudyProgram(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    @property
    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Study Program"
        verbose_name_plural = "Study Programs"


class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    img_url = models.CharField(max_length=2000, null=True, blank=True)

    @property
    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"


class StudyProgramInUniversity(models.Model):
    offline, online = 'OFFLINE', 'ONLINE'
    bachelor, master = 'bachelor', 'master'
    FORM_OF_STUDY = (
        (offline, 'Offline'),
        (online, 'Online')
    )

    DEGREE = (
        (bachelor, 'Bachelor'),
        (master, 'Master')
    )

    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=5, null=True, blank=True)
    scholarship_availability = models.BooleanField(default=False)
    scholarship_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    duration_in_month = models.IntegerField(null=True, blank=True)
    duration = models.CharField(max_length=255, null=True, blank=True)
    form_of_study = models.CharField(max_length=10, choices=FORM_OF_STUDY, null=True, blank=True)
    degree = models.CharField(max_length=10, choices=DEGREE, null=True, blank=True)
    start_of_study = models.CharField(max_length=255, blank=True, null=True)

    study_program = models.ForeignKey(StudyProgram, on_delete=models.CASCADE, related_name="university_study_programs")
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="university_study_programs")

    @property
    def slug(self):
        return slugify(f"{self.degree} {self.study_program.name} {self.university.name}")

    def __str__(self):
        return f"{self.degree} of {self.study_program.name} in {self.university.name}"

    class Meta:
        verbose_name = "University Study Program"
        verbose_name_plural = "University Study Programs"
