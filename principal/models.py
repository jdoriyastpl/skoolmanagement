from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.validators import RegexValidator
# Create your models here.
User = settings.AUTH_USER_MODEL
NAME_REGEX = '^[a-zA-Z]*$'
PHONE_REGEX ='^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$'

class Principal(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=15, blank=False,
                                  validators=[
                                        RegexValidator(
                                        regex = NAME_REGEX,
                                        message = 'Name must be Alphabetic',
                                        code='invalid_first_name'
                                        )])
    dob = models.DateTimeField(auto_now_add=True)
    phone_number =models.CharField(max_length=10,unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    picture = models.ImageField(null=True,
                                blank=True,
                                default='principal/img/default.png',
                                height_field="height_field",
                                width_field="width_field",
                                verbose_name="profile picture"
                                )
    height_field = models.IntegerField(default=600, null=True)
    width_field = models.IntegerField(default=600, null=True)
