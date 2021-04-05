from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
class UserAdminSite(admin.AdminSite):
  site_header = 'Users Admin Page'
  site_title = 'Users Admin Portal'
  index_title = 'Welcome to Users Admin Page'

user_admin_site = UserAdminSite(name='users_admin')
user_admin_site.register(User)
