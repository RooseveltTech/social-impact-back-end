from django.contrib.auth import get_user_model
from import_export import resources
from air_quality_app.models import AllPlantTable, Blog, Forum, Comment

User = get_user_model()


class AllPlantTableResource(resources.ModelResource):
    class Meta:
        model = AllPlantTable

class BlogResource(resources.ModelResource):
    class Meta:
        model = Blog

class ForumResource(resources.ModelResource):
    class Meta:
        model = Forum
        
class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment