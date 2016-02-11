from django.shortcuts import render,get_object_or_404
from points.models import Points
from points.forms import AddPoint
from wusers.models import Wusers
from places.models import Places
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
import os
import json

# Create your views here.

def index(request):
    return render(request,"points/index.html",{})

def addpoint(request,place_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        if request.method=="POST":
            form=AddPoint(request.POST)
            if form.is_valid():
                title=form.cleaned_data["title"]
                description=form.cleaned_data["description"]
                place=get_object_or_404(Places,pk=place_id)
                point=Points(title=title,description=description,user=request.user,place=place)
                point.save()
                return HttpResponseRedirect(reverse('viewplace',args=[place_id]))
            else:
                return render(request,"points/addpoint.html",{'form':form})
        else:
            form=AddPoint()
            return render(request,"points/addpoint.html",{'form':form})

def handlepointvote(request,point_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        json_data=json.loads(request.body)
        print json_data
        mark_type=json_data["type"]
        vote_action=json_data["action"]
        point=get_object_or_404(Points,pk=point_id)
        thisUserUpvote=point.marked_as_right.filter(id=request.user.id).count()
        thisUserDownvote=point.marked_as_wrong.filter(id=request.user.id).count()
        if vote_action=="vote":
            if thisUserUpvote==0 and thisUserDownvote==0:
                if mark_type=="right":
                    point.marked_as_right.add(request.user)
                elif mark_type=="wrong":
                    point.marked_as_wrong.add(request.user)
                else:
                    return HttpResponse("error-unknown mark-type")
        elif vote_action=="recall-vote":
            if mark_type=="right" and thisUserUpvote==1:
                point.marked_as_right.remove(request.user)
            elif mark_type=="wrong" and thisUserDownvote==1:
                point.marked_as_wrong.remove(request.user)
            else:
                return HttpResponse("error-unknow mark-type")
        else:
            return HttpResponse("error bad-action")
        num=0
        if mark_type=="right":
            num=point.marked_as_right.count()
        else:
            num=point.marked_as_wrong.count()
        return HttpResponse(num)
