from django.db import models
from account.models import User
# Create your models here.


class Standard(models.Model):
    user = models.ForeignKey(User,related_name='principal_class')
    standard = models.CharField(max_length=200)
    no_students = models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.standard
