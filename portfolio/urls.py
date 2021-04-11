from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.project_index, name='project_index'),
    path('index/<int:pk>/', views.project_detail, name='project_detail')
]
