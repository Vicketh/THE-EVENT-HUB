from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('categories/', views.category_list, name='category_list'),
    path('users/', views.user_list, name='user_list'),
]
