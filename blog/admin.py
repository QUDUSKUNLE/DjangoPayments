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

# admin.site.register(Post, PostAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Comment, CommentAdmin)
