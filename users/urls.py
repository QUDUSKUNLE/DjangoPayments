from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
  url(r'^dashboard/', views.dashboard, name='dashboard'),
  url(r'^register/', views.register, name='register'),
  url(r'^accounts/', include('django.contrib.auth.urls')),
  url(r'^oauth/', include('social_django.urls')),
  path('see_request/', views.see_request),
  path('see_userinfo/', views.user_info),
  path('private_route', views.private_route),
  path('staff_place/', views.staff_place),
  path('add_messages/', views.add_messages),
]
