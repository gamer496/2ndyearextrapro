from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Wusers(models.Model):
    user            =models.OneToOneField   (User)
    reputation      =models.IntegerField    (default=0)
    country         =models.CharField       (default=None,max_length=100)
    activation_key  =models.CharField       (max_length=40,default="NONE")
    key_expires     =models.DateTimeField   (default=timezone.now)


    def __unicode__(self):
        return self.user.username
