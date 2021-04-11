from django.urls import path
from . import views
from .admin import comment_admin_site, post_admin_site, category_admin_site


urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<category>/', views.blog_category, name='blog_category'),
    path('categories-admin', category_admin_site.urls),
    path('posts-admin', post_admin_site.urls),
    path('comments-admin', comment_admin_site.urls),
]
