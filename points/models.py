from __future__ import unicode_literals

from django.db import models
from places.models import Places
from wusers.models import Wusers
from django.contrib.auth.models import User

class Points(models.Model):
    user            =models.ForeignKey      (User,related_name="userwhocreatedthepoint")
    place           =models.ForeignKey      (Places,related_name="pointofplace")
    description     =models.TextField       ()
    title           =models.CharField       (max_length=200)
    marked_as_right =models.ManyToManyField (User,blank=True,related_name="userswhomarkedright")
    marked_as_wrong =models.ManyToManyField (User,blank=True,related_name="userswhomarkedwrong")

    def __unicode__(self):
        return self.title
