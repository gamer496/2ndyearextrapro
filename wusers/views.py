from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from wusers.forms import RegistrationForm
from wusers.models import Wusers
from django.http import HttpResponseRedirect,HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import password_reset,password_reset_confirm
from django.core.urlresolvers import reverse
import datetime
import os
import hashlib
import random

def index(request):
    return render(request,"wusers/index.html",{})

def registration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        if request.method=="POST":
            form=RegistrationForm(request.POST)
            if form.is_valid():
                datas={}
                datas['username']   =form.cleaned_data['username']
                datas['password']   =form.cleaned_data['password']
                datas['first_name'] =form.cleaned_data['first_name']
                datas['last_name']  =form.cleaned_data['last_name']
                datas['email']      =form.cleaned_data['email']
                datas['country']    =form.cleaned_data['country']
                salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
                usernamesalt=datas['username']
                if isinstance(usernamesalt,unicode):
                    usernamesalt=usernamesalt.encode('utf8')
                datas['activation_key']=hashlib.sha1(salt+usernamesalt).hexdigest()
                datas['email_path']="ActivationEmail.txt"
                datas['email_subject']="Activation of your registration"
                form.sendEmail(datas)
                form.save(datas)
                request.session['registered']=True
                return HttpResponseRedirect("/")
            else:
                return render(request,"wusers/registration.html",{'form':form})
        else:
            form=RegistrationForm()
            return render(request,"wusers/registration.html",{'form':form})

def activation(request,key):
    activation_expired=False
    already_active=False
    wuser=get_object_or_404(Wusers,activation_key=key)
    if wuser.user.is_active==False:
        if timezone.now()>wuser.key_expires:
            activation_expired=True
            id_user=wuser.user.id
        else:
            wuser.user.is_active=True
            wuser.user.save()
    else:
        already_active=True
    return HttpResponseRedirect("/")

def new_activation_link(request,user_id):
    form=RegistrationForm()
    datas={}
    user=User.objects.get(id=user_id)
    if user is not None and not user.is_active:
        datas['username']=user.username
        datas['email']=user.email
        datas['first_name']=user.first_name
        datas['last_name']=user.last_name
        datas['email_path']="ResendEmail.txt"
        datas['email_subject']="Email for activation"
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        usernamesalt=datas['username']
        if isinstance(usernamesalt,unicode):
            usernamesalt=usernamesalt.encode('utf8')
        datas['activation_key']=hashlib.sha1(salt+usernamesalt).hexdigest()
        wuser=Wusers.objects.get(user=user)
        wuser.activation_key=datas['activation_key']
        datas['country']=wuser.country
        wuser.key_expires=datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")
        wuser.save()
        form.sendEmail(datas)
        request.session['new_link']=True
    return HttpResponseRedirect("/")

def wuser_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    elif request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect("/")
        else:
            return render(request,"wusers/login.html",{})
    else:
        return render(request,"wusers/login.html",{})

def wuser_logout(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        logout(request)
        return HttpResponseRedirect(reverse("userlogin"))

def reset(request):
    return password_reset(request,template_name=os.path.join("wusers","reset.html"),email_template_name="reset_email.html",subject_template_name="reset_subject.txt",post_reset_redirect=reverse("successrequest"))

def reset_confirm(request,uidb64=None,token=None):
    return password_reset_confirm(request, template_name=os.path.join("wusers","reset_confirm.html"),uidb64=uidb64, token=token, post_reset_redirect=reverse('success'))

def success(request):
    return render(request,"wusers/success.html",{})

def succeessrequest(request):
    return render(request,"wusers/successrequest.html",{})

def viewprofile(request,wuser_id):
    wuser=get_object_or_404(Wusers,pk=wuser_id)
    own_id=False
    if wuser.user==request.user:
        own_id=True
    return render(request,"wusers/viewprofile.html",{'wuser':wuser,'own_id':own_id})
