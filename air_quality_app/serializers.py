from rest_framework import serializers

from air_quality_app.models import AllPlantTable, Blog, Comment, Forum


class ListPlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllPlantTable
        fields = (
            "id",
            "name",
            "botanical_name",
            "toxicity_level",
            "plan_removes_toxins",
            "plant_care",
            "created_at",
            "image"
        )
    def to_representation(self, obj):
        serialized_data = super().to_representation(obj)
        image = f"https://res.cloudinary.com/dqjmovcjo/{serialized_data['image']}" if serialized_data['image'] is not None else None
        serialized_data["image"] =  image
        return serialized_data

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            "id",
            "blog_title",
            "blog_user",
            "blog_body",
            "created_at",
            "count",
            "image",
        )

    def to_representation(self, instance):
        serialized_data = super().to_representation(instance)
        serialized_data["first_name"] = instance.blog_user.first_name
        serialized_data["last_name"] = instance.blog_user.last_name
        image = f"https://res.cloudinary.com/dqjmovcjo/{serialized_data['image']}" if serialized_data['image'] is not None else None
        serialized_data["image"] =  image
        return serialized_data

class ForumPostSerializer(serializers.Serializer):
    post = serializers.CharField(required=True)

class ViewForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = (
            "id",
            "forum_user",
            "forum_body",
            "created_at",
        )

    def to_representation(self, instance):
        serialized_data = super().to_representation(instance)
        serialized_data["first_name"] = instance.forum_user.first_name
        serialized_data["last_name"] = instance.forum_user.last_name

        return serialized_data

class ForumCommentSerializer(serializers.Serializer):
    comment = serializers.CharField(required=True)
    forum_id = serializers.CharField(required=True)

class ViewForumCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "user",
            "blog",
            "forum",
            "body",
            "created_at",
        )

    def to_representation(self, instance):
        serialized_data = super().to_representation(instance)
        serialized_data["first_name"] = instance.user.first_name
        serialized_data["last_name"] = instance.user.last_name
        serialized_data["forum_id"] = instance.forum.id

        return serialized_data