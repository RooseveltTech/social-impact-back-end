from django.contrib import admin


# Register your models here.

from import_export.admin import ImportExportModelAdmin
# from air_quality_app.models import AllPlantTable, Blog, Forum, Comment
from .resources import *


class AllPlantTableResourceAdmin(ImportExportModelAdmin):
    resource_class = AllPlantTableResource
    # search_fields = [""]

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
    
class BlogResourceAdmin(ImportExportModelAdmin):
    resource_class = BlogResource
    # search_fields = [""]

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
    
class ForumResourceAdmin(ImportExportModelAdmin):
    resource_class = ForumResource
    # search_fields = [""]

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
    
class CommentResourceAdmin(ImportExportModelAdmin):
    resource_class = CommentResource
    # search_fields = [""]

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
    
    def approve_comments(self, request, queryset):
        queryset.update(active=True)
    
    
admin.site.register(AllPlantTable, AllPlantTableResourceAdmin)
admin.site.register(Blog, BlogResourceAdmin)
admin.site.register(Forum, ForumResourceAdmin)
admin.site.register(Comment, CommentResourceAdmin)