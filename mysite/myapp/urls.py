from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'comments/', include('django_comments_xtd.urls')),
    path(r'markdownx/', include('markdownx.urls')),
    path('chat/', views.chat, name='chat'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('<str:category_name>/', views.category, name='category'),
    path('<str:resources_category>/<str:resources_title>/', views.resource, name='resource'),
    path('<str:resources_category>/<str:resources_title>/<str:guide_title>/', views.guide, name='guide')
] 