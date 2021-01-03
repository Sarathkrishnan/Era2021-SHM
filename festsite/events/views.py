from django.shortcuts import render
from django.http import HttpResponse

from .models import Events

# Create your views here.
def home(request):
    allevents = Events.objects.all()
    context={}
    context['allevents']=allevents
    return render(request,'home.html',context)
def event(request,event_id):
    context={}
    context['event']=Events.objects.get(pk=event_id)

    return render(request, 'event.html',context)