from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from wusers.models import Wusers

class Messages(models.Model):
    sender      =models.ForeignKey      (Wusers,related_name="wuserwhosend")
    receiver    =models.ForeignKey      (Wusers,related_name="wuserswhoreceived")
    timesent    =models.DateTimeField   (default=timezone.now)
    message     =models.TextField       ()
    seen        =models.BooleanField    (default=False)

    def __unicode__(self):
        return self.message
