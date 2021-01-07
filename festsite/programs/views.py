from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Festevent, EventRegistration

from .forms import Register
# Create your views here.
def index(request):
    allevents = Festevent.objects.all()
    context={'allevents':allevents}
    return render(request, 'index.html', context)

def event(request,event_id):
    selected_event = Festevent.objects.get(pk=event_id)
    context={'selected_event':selected_event}
    return render(request,'event.html',context)

def register(request,event_id):
    selected_event = Festevent.objects.get(pk=event_id)
    context={'selected_event':selected_event}
    if request.POST:
        form = Register(request.POST)
        context['form'] = form

  

        if form.is_valid():
            form.save()
            #return redirect('home')
            return HttpResponse('Registration success')
        else:
            return HttpResponse('Registration fails')
            #form = Register()
            #context['form'] = form
    else:
        form =Register(
            initial={
                'event':event_id,
                'first_name':'',
                'second_name':'',
                'email':'',
                'phone':'',
                'course':'','year':'',
                'college':'',
            }
        )
    context={'selected_event':selected_event,'form':Register}
    return render(request,'register.html',context)