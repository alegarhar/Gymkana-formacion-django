from django.shortcuts import render, loader

# Create your views here.
from django.http import HttpResponse

from .models import New, Event


def index(request):
    latest_news_list = New.objects.order_by('-id')[:3]
    latest_events_list = Event.objects.order_by('-id')[:3]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_news_list': latest_news_list,
        'latest_events_list': latest_events_list,
    }
    return HttpResponse(template.render(context, request))