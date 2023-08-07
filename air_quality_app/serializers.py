from rest_framework import serializers

from air_quality_app.models import AllPlantTable, Blog


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

        return serialized_data


    
    

