from django.db import models
from account.models import User
from django.urls import reverse

# Create your models here.


class Standard(models.Model):
    user = models.ForeignKey(User,related_name='principal_class')
    name = models.CharField(max_length=200,unique= True)


    def get_absolute_url(self):
        return reverse("standard:detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
