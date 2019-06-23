from django.urls import path
from . import views


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('v1/news/create', views.news_create, name='news_create'),
]
