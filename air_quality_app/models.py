from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
User = get_user_model()

# Create your models here.
class AllPlantTable(models.Model):
    """All Plants."""

    TOXICITY_LEVEL = [
        ("LOW", "LOW"),
        ("MEDIUM", "MEDIUM"),
        ("HIGH", "HIGH"),
    ]
    TYPE_BY_SIZE = [
        ("Herbs", "Herbs"),
        ("Shrubs", "Shrubs"),
        ("Trees", "Trees"),
        ("Herbaceous", "Herbaceous"),
        ("Creepers", "Creepers"),
        ("Climbers", "Climbers"),
    ]
    LIFE_CYCLE = [
        ("Perennial", "Perennial"),
        ("Annual", "Annual"),
        ("Bi-Annual", "Bi-Annual"),
    ]
    name = models.CharField(max_length=500)
    botanical_name = models.CharField(max_length=500, blank=True, null=True)
    type_by_size = models.CharField(max_length=500, choices=TYPE_BY_SIZE, blank=True, null=True)
    type_by_life_cycle = models.CharField(max_length=500, choices=LIFE_CYCLE, blank=True, null=True)
    plant_care = models.TextField(blank=True, null=True)
    toxicity = models.TextField(blank=True, null=True)
    toxicity_level = models.CharField(max_length=500,choices=TOXICITY_LEVEL, blank=True, null=True)
    plan_removes_toxins = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', default="image/upload/v1677969748/sample.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return name."""
        return self.name
    

class Blog(models.Model):
    """All Plants."""

    blog_title = models.CharField(max_length=500, blank=True, null=True)
    blog_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    blog_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
    image = CloudinaryField('image', default="image/upload/v1677969748/sample.jpg")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return 'Blog {} by {}'.format(self.blog_body, self.blog_user.username)
    
class Forum(models.Model):

    forum_title = models.CharField(max_length=500, blank=True, null=True)
    forum_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    forum_body = models.TextField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comments', blank=True, null=True)
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE,related_name='forum_comments', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user.username)