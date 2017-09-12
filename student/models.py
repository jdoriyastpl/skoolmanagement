from django.db import models
from standard.models import Standard
from section.models import Section
from django.core.validators import RegexValidator
# Create your models here.
PHONE_REGEX ='^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$'
class Student(models.Model):
    name = models.CharField(max_length=250)
    standard = models.ForeignKey(Standard, related_name ='student_standard')
    section = models.ForeignKey(Section,related_name ='student_section')
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    RELIGION = (
        ('hindu','Hinduism'),
        ('muslim','Muslim'),
        ('christian','Christian'),
        ('sikh','Sikh')
    )
    created_date = models.DateTimeField(auto_now_add=True)
    religion = models.CharField(max_length=10, choices=RELIGION,blank=True,verbose_name="Religion")
    parents_primary_phone_number = models.CharField(max_length=10,unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    secondary_phone_number = models.CharField(max_length=10,unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    address = models.CharField(max_length=255)
    picture = models.ImageField(null=True,
                                blank=True,
                                default='student/img/default.png',
                                height_field="height_field",
                                width_field="width_field",
                                verbose_name="profile picture"
                                )
    height_field = models.IntegerField(default=600, null=True)
    width_field = models.IntegerField(default=600, null=True)

    def get_absolute_url(self):
        return reverse("student:detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
