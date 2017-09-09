from django.db import models
from account.models import User
from django.utils.text import slugify
from django.urls import reverse

from django import template
register = template.Library()

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode= True,unique=True)
    description = models.TextField(blank=True,default='')
    member = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug'=self.slug})



class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name="memberships")
    user = models.ForeignKey(User,related_name='user_groups')

    def __str__(self):
        return self.user.username
    class Meta:
        unique_together = ('group','user')
