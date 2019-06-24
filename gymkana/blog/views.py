from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
# Create your views here.

from .models import New, Event
from .forms import NewNews


def index(request):
    latest_news_list = New.objects.order_by('-id')[:3]
    latest_events_list = Event.objects.order_by('-id')[:3]
    context = {
        'latest_news_list': latest_news_list,
        'latest_events_list': latest_events_list,
    }
    return render(request, 'blog/index.html', context)


def news_create(request):
    form = NewNews()
    if request.method == 'POST':
        form = NewNews(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'blog/post_create.html', {'form': form})


def news_view(request):
    news_list = New.objects.all()
    context = {
        'news_list': news_list,
    }
    return render(request, 'blog/news_view.html', context)


def news_view_detail(request, news_id):
    news = get_object_or_404(New, pk=news_id)
    return render(request, 'blog/news_view_detail.html', {'news': news})


def news_edit(request, news_id):
    aux = get_object_or_404(New, pk=news_id)
    if request.method == 'POST':
        form = NewNews(request.POST or None, files=request.FILES or None, instance=aux)
        if form.is_valid():
            form.save()
    else:
        form = NewNews(instance=aux, initial={'news_id': news_id})
    return render(request, 'blog/news_edit.html', {'form': form})


def news_delete(request, news_id):
    aux = get_object_or_404(New, pk=news_id)
    if request.method == 'POST':
        aux.image.delete()
        aux.delete()
        return redirect('news_view')
    return render(request, 'blog/news_delete.html')


class NewsCreate(CreateView):
    template_name = 'blog/post_create.html'
    form_class = NewNews
    success_url = 'create'


class NewsView(TemplateView):
    template_name = 'blog/news_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = New.objects.all()
        return context
