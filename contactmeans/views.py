from django.shortcuts import render,get_object_or_404
from contactmeans.forms import MessageForm
from wusers.models import Wusers
from contactmeans.models import Messages

def index(request):
    return (request,"messages/index.html",{})

def SendMessage(request,receiver_id):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        if request.method=="POST":
            form=MessageForm(request.POST)
            if form.is_valid():
                message=form.cleaned_data()
                sender=get_object_or_404(Wusers,user=request.user)
                receiver=get_object_or_404(Wusers,pk=receiver_id)
                message=Messages(message=message,sender=sender,receiver=receiver)
                message.save()
                return HttpResponseRedirect(reverse('messagesent'))
            else:
                return render(request,"messages/sendmessage.html",{'form':form})
        else:
            form=MessageForm()
            return render(request,"messages/viewmessage.html",{'form':form})

def messagesent(request):
    return render(request,"messages/messagesent.html",{})

def viewreceivedmessages(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        user=request.user
        wuser=get_object_or_404(Wusers,user=request.user)
        allmessages=wuser.wuserswhoreceived.all()
        return render(request,"messages/viewreceivedmessages.html",{'allmessages':allmessages})

def viewsentmessages(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        user=request.user
        wuser=get_object_or_404(Wusers,user=user)
        allmessages=wuser.wuserwhosend.all()
        return render(request,"messages/viewsentmessages.html",{'allmessages':allmessages})
