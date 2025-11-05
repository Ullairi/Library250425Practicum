from django.db import models
from django.db.models.fields import CharField
from django.template.defaultfilters import first

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.last_name[0]}. {self.first_name}"


