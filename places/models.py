from __future__ import unicode_literals

from django.db import models
from wusers.models import Wusers
from django.contrib.auth.models import User

# Create your models here.

class Places(models.Model):
    user            =models.ForeignKey      (User,related_name="userwhocreatedtheplace")
    country         =models.CharField       (max_length=100)
    state           =models.CharField       (max_length=100)
    city            =models.CharField       (max_length=100)
    address         =models.CharField       (max_length=230)
    company         =models.CharField       (max_length=250)
    usersupvoted    =models.ManyToManyField (User,blank=True,related_name="userswhoupvoted")
    usersdownvoted  =models.ManyToManyField (User,blank=True,related_name="userswhodownvoted")


    def __unicode__(self):
        return self.company
