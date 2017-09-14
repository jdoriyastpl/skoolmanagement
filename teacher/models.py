from django.db import models
from account.models import User
from django.urls import reverse
from django.core.validators import RegexValidator
from django.utils import timezone
from datetime import datetime

PHONE_REGEX ='^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$'
# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, related_name='users_teacher')
    name = models.CharField(max_length=255)
    phone_number =models.CharField(max_length=10,unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    created_date = models.DateTimeField(default=timezone.now)
    subject = models.CharField(max_length=150)
    address = models.CharField(max_length=255,null=False)
    age = models.PositiveIntegerField(null= False,verbose_name="Teacher Age")
    picture = models.ImageField(null=True,
                                blank=True,
                                default='teacher/img/default.png',
                                height_field="height_field",
                                width_field="width_field",
                                verbose_name="profile picture"
                                )
