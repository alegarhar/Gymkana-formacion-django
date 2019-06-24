from django.urls import path
from . import views


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('v1/news/create', views.news_create, name='news_create'),
    path('v1/news/view', views.news_view, name='news_view'),
    path('v1/news/view/<int:news_id>', views.news_view_detail, name='news_view_detail'),
    path('v1/news/view/edit/<int:news_id>', views.news_edit, name='news_edit'),
]
