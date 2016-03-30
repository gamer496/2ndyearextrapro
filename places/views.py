from django.shortcuts import render,get_object_or_404
from places.forms import AddPlace
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from places.models import Places
from wusers.models import Wusers
from points.models import Points
import json


def index(request):
    return render(request,"places/index.html",{})

def addplace(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        if request.method=="POST":
            form=AddPlace(request.POST)
            if form.is_valid():
                place=Places(user=request.user,country=form.cleaned_data['country'],state=form.cleaned_data['state'],city=form.cleaned_data['city'],company=form.cleaned_data['company'],address=form.cleaned_data['address'])
                place.save()
                return HttpResponseRedirect(reverse("viewplaces"))
            else:
                return render(request,"places/addplace.html",{'form':form})
        else:
            form=AddPlace()
            return render(request,"places/addplace.html",{'form':form})

def viewplaces(request):
    places=Places.objects.all()
    return render(request,"places/viewplaces.html",{'places':places})

def viewplace(request,id):
    place=get_object_or_404(Places,id=id)
    points=place.pointofplace.all()
    user=request.user
    count=place.usersupvoted.count()-place.usersdownvoted.count()
    thisUserUpvote=place.usersupvoted.filter(id=user.id).count()
    thisUserDownvote=place.usersdownvoted.filter(id=user.id).count()
    print thisUserUpvote,thisUserDownvote
    infos=[]
    for point in points:
        thisUserUpvotepoint=point.marked_as_right.filter(id=user.id).count()
        thisUserDownvotepoint=point.marked_as_wrong.filter(id=user.id).count()
        infos.append([point,thisUserUpvotepoint,thisUserDownvotepoint])
    if not place:
        return HttpResponseRedirect("/")
    else:
        return render(request,"places/viewplace.html",{'place':place,'count':count,'thisUserUpvote':thisUserUpvote,'thisUserDownvote':thisUserDownvote,'infos':infos})


def placevote(request):
    json_data=json.loads(request.body)
    print json_data
    place_id=int(json_data["id"])
    vote_type=json_data["type"]
    vote_action=json_data["action"]
    place=get_object_or_404(Places,pk=place_id)
    thisUserUpvote=place.usersupvoted.filter(id=request.user.id).count()
    thisUserDownvote=place.usersdownvoted.filter(id=request.user.id).count()
    if vote_action=='vote':
        if thisUserUpvote==0 and thisUserDownvote==0:
            if vote_type=='up':
                place.usersupvoted.add(request.user)
            elif vote_type=='down':
                place.usersdownvoted.add(request.user)
            else:
                return HttpResponse('error-unknown vote-type maybe the json wasnt passed correctly')
    elif vote_action=='recall-vote':
        if vote_type=="up" and thisUserUpvote==1:
            place.usersupvoted.remove(request.user)
        elif vote_type=="down" and thisUserDownvote==1:
            place.usersdownvoted.remove(request.user)
        else:
            return HttpResponse('error-unknown vote-type maybe the json wasnt passed correctly')
    else:
        return HttpResponse("error bad-action maybe the json wasnt passed correctly")
    num_votes=place.usersupvoted.count()-place.usersdownvoted.count()
    return HttpResponse(num_votes)
