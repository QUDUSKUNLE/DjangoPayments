from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  pass


class PostAdminSite(admin.AdminSite):
  site_header = 'Posts Admin Page'
  site_title = 'Posts Admin Portal'
  index_title = 'Welcome to Posts Admin Page'

post_admin_site = PostAdminSite(name='posts_admin')
post_admin_site.register(Post)


class CategoryAdminSite(admin.AdminSite):
  site_header = 'Category Admin Page'
  site_title = 'Category Admin Portal'
  index_title = 'Welcome to Category Admin Page'

category_admin_site = CategoryAdminSite(name='categories_admin')
category_admin_site.register(Category)


class CommentAdminSite(admin.AdminSite):
  site_header = 'Comments Admin Page'
  site_title = 'Comments Admin Portal'
  index_title = 'Welcome to Comments Admin Page'

comment_admin_site = CommentAdminSite(name='comments_admin')
comment_admin_site.register(Comment)
# admin.site.register(Post, PostAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Comment, CommentAdmin)
