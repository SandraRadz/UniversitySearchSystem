from django.db import models
from django.template.defaultfilters import slugify


class Country(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

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

    def __str__(self):
        return self.name
