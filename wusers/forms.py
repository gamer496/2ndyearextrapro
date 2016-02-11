from django import forms
from django.contrib.auth.models import User
from wusers.models import Wusers
from workplace_data import settings
from django.template import Template,Context
from django.shortcuts import render
from django.core.mail import send_mail
import os
import datetime
import hashlib

class RegistrationForm(forms.ModelForm):
    password    =forms.CharField    (widget=forms.PasswordInput())
    username    =forms.CharField    ()
    email       =forms.EmailField   ()
    first_name  =forms.CharField    (required=False)
    last_name   =forms.CharField    (required=False)

    class Meta:
        model=Wusers
        exclude=('user','reputation','activation_key','key_expires')

    def save(self,datas):
        u=User.objects.create_user(username=datas['username'],email=datas['email'],first_name=datas['first_name'],last_name=datas['last_name'])
        u.set_password(datas['password'])
        u.is_active=False
        u.save()
        wuser=Wusers(user=u,country=datas['country'],activation_key=datas['activation_key'],key_expires=datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S"))
        wuser.save()
        return u

    def sendEmail(self,datas):
        link="http://127.0.0.1:8000/wusers/activate/"+datas['activation_key']
        c=Context({'activation_link':link,'username':datas['username']})
        f=open(os.path.join(settings.TEMPLATE_DIR,datas['email_path']),'r')
        t=Template(f.read())
        f.close()
        message=t.render(c)
        send_mail(datas['email_subject'],message,'somedomain',[datas['email']],fail_silently=False)
