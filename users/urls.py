from django.conf.urls import include, url
from . import views

urlpatterns = [
  url(r'^dashboard/', views.dashboard, name='dashboard'),
  url(r'^register/', views.register, name='register'),
  url(r'^accounts/', include('django.contrib.auth.urls')),
  url(r'^oauth/', include('social_django.urls')),
]