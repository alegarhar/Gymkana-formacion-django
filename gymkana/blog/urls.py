from django.urls import path
from . import views


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('v1/news/create', views.news_create, name='news_create'),
    path('v1/news/view', views.news_view, name='news_view'),
    path('v1/news/view/<int:news_id>', views.news_view_detail, name='news_view_detail'),
    path('v1/news/view/edit/<int:news_id>', views.news_edit, name='news_edit'),
    path('v1/news/view/delete/<int:news_id>', views.news_delete, name='news_delete'),
    path('v2/news/create', views.NewsCreate.as_view(), name='news_create_class'),
    path('v2/news/view', views.NewsView.as_view(), name='news_view_class'),
    path('v2/news/view/<int:news_id>', views.NewsViewDetail.as_view(), name='news_view_detail_class'),
    path('v2/news/view/edit/<int:pk>', views.NewsEdit.as_view(), name='news_edit_class'),
    path('v2/news/view/delete/<int:pk>', views.NewsDelete.as_view(), name='news_delete_class'),
]
