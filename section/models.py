from django.db import models
from standard.models import Standard
# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=100,unique=True)
    standard = models.ForeignKey(Standard,related_name='standard_section')
    no_students = models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.name
