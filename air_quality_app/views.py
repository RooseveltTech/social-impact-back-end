from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from air_quality_app.apis.call_api import AirQuality
from air_quality_app.apis.func import CustomPaginator, get_aqi_status, get_ip_address
from air_quality_app.models import AllPlantTable, Blog, Comment, Forum
from air_quality_app.serializers import BlogSerializer, ForumCommentSerializer, ForumPostSerializer, ListPlantsSerializer, ViewForumCommentSerializer, ViewForumSerializer
from drf_yasg.utils import swagger_auto_schema
from air_quality_app.api_params import ApiParams
# Create your views here.



class AirQualityAPIVIew(APIView):
    permission_classes = [IsAuthenticated]
    """Air Quality API View."""

    def get(self, request):
        # ip_addr = get_ip_address(request)
        # print(ip_addr)
        # city = AirQuality.get_city(ip_addr)
        # print(city)
        city = "Lagos"

        all_plants = AllPlantTable.objects.all()  
        serializer = ListPlantsSerializer(all_plants, many=True)
        response = AirQuality.get_quality_data(city)
        if response.get("status") == "ok":
            aqi = response.get("data").get("aqi")
            idx = response.get("data").get("idx")
            city = response.get("data").get("city").get("name")
            aqi_status, aqi_color, aqi_message = get_aqi_status(aqi)
            return Response(
                {
                "aqi": aqi,
                "idx": idx,
                "city": city,
                "aqi_status": aqi_status, 
                "aqi_color": aqi_color,
                "aqi_message": aqi_message,
                "all_plants": serializer.data,

            },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "air_quality": response,
                    "all_plants": serializer.data,
                },
                status=status.HTTP_200_OK
            )
        

class AirPlantsAPIVIew(APIView):
    permission_classes = [IsAuthenticated]
    """Get Plant details API View."""
    @swagger_auto_schema(manual_parameters=[ApiParams.plant_id])
    def get(self, request):
        plant_id = request.query_params.get("plant_id")
        try:
            single_plant = AllPlantTable.objects.filter(id=plant_id).first()
            if single_plant:
                return Response(
                    {
                        "status": "success",
                        "id" : single_plant.id,
                        "name": single_plant.name,
                        "botanical_name": single_plant.botanical_name,
                        "type_by_size": single_plant.type_by_size,
                        "type_by_life_cycle": single_plant.type_by_life_cycle,
                        "plant_care": single_plant.plant_care, 
                        "toxicity": single_plant.toxicity,
                        "toxicity_level": single_plant.toxicity_level, 
                        "plan_removes_toxins": single_plant.plan_removes_toxins,
                        "description": single_plant.description, 
                        "image": f"https://res.cloudinary.com/dqjmovcjo/{single_plant.image}" if single_plant.image is not None else None,
                },
                status=status.HTTP_200_OK)
            else:
                return Response(
                    {
                        "status": "error",
                        "message": "plant not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        except ValueError:
            return Response(
                {
                    "status": "error",
                    "message": "plant not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
       
class Blogs(APIView):
    """Blog API View."""
    @swagger_auto_schema(manual_parameters=[ApiParams.page])
    def get(self, request):
        page = request.GET.get("page", 1)
        blogs = Blog.objects.all().order_by('-created_at')
        blog_list = CustomPaginator.paginate(
            request, blogs, page
        )
        serializer = BlogSerializer(blog_list, many=True)
        try:
        
            data = {
                "data_type": "BLOG",
                "data": serializer.data,
                "total_page":  blog_list.paginator.num_pages,
                "page_count": len(serializer.data),
                "total_data_count":  blog_list.paginator.count,
            }
        except AttributeError:
            data = {
                "data_type": "BLOG",
                "data": [],
                "total_page": 0,
                "page_count": len(serializer.data),
                "total_data_count": 0,
            }
        return Response(data, status=status.HTTP_200_OK)
    
class SingleBlogAPIView(APIView):
    """single Blog API View."""
    @swagger_auto_schema(manual_parameters=[ApiParams.blog_id])
    def get(self, request):
        blog_id = request.query_params.get("blog_id")
        try:
            single_blog = Blog.objects.filter(id=blog_id).first()
            if single_blog:
                return Response(
                    {
                        "status": "success",
                        "id" : single_blog.id,
                        "blog_title": single_blog.blog_title,
                        "first_name": single_blog.blog_user.first_name,
                        "last_name": single_blog.blog_user.last_name,
                        "count": single_blog.count,
                        "blog_body": single_blog.blog_body,
                        "image": single_blog.image,
                        "created_at": single_blog.created_at
                },
                status=status.HTTP_200_OK)
            else:
                return Response(
                    {
                        "status": "error",
                        "message": "blog not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        except ValueError:
            return Response(
                {
                    "status": "error",
                    "message": "blog not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
class LikeBlogAPIView(APIView):
    """Like Blog API View."""
    @swagger_auto_schema(manual_parameters=[ApiParams.blog_id])
    def get(self, request):
        blog_id = request.query_params.get("blog_id")
        try:
            single_blog = Blog.objects.filter(id=blog_id).first()
            if single_blog:
                single_blog.count+=1
                single_blog.save()
            else:
                pass
        except ValueError:
            pass
        return Response({"message":"successful"},status=status.HTTP_200_OK)
           
       
class CheckUserAPIView(APIView):
    """Check User API View."""
    permission_classes = [IsAuthenticated]    
    def get(self, request):
        user = request.user
        return Response({"success":"OK"}, status=status.HTTP_200_OK)

class ForumPostAPIView(APIView):
    """Check User API View."""
    permission_classes = [IsAuthenticated]    
    def post(self, request):
        user = request.user
        serializer = ForumPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.validated_data.get("post")
        print(post)
        Forum.objects.create(
            forum_user=user,
            forum_body=post
        )
        return Response({"success":"OK"}, status=status.HTTP_200_OK)

class GetAllForumPostAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page = request.query_params.get("page", 1)
        forum_post = Forum.objects.all().filter(active=True).order_by('-created_at')
        forum_list = CustomPaginator.paginate(
            request, forum_post, page
        )
        serializer = ViewForumSerializer(forum_list, many=True)
        try:
        
            data = {
                "data_type": "Forum",
                "data": serializer.data,
                "total_page":  forum_list.paginator.num_pages,
                "page_count": len(serializer.data),
                "total_data_count":  forum_list.paginator.count,
            }
        except AttributeError:
            data = {
                "data_type": "Forum",
                "data": [],
                "total_page": 0,
                "page_count": len(serializer.data),
                "total_data_count": 0,
            }
        return Response(data, status=status.HTTP_200_OK)

class ForumCommentAPIView(APIView):
    """Check User API View."""
    permission_classes = [IsAuthenticated]    
    def post(self, request):
        user = request.user
        serializer = ForumCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.validated_data.get("comment")
        forum_id = serializer.validated_data.get("forum_id")
        get_forum = Forum.objects.filter(id=forum_id).first()
        if get_forum:
            Comment.objects.create(
                forum=get_forum,
                user=user,
                body=comment
            )
        return Response({"success":"OK"}, status=status.HTTP_200_OK)

class GetAllForumCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        forum_id = request.query_params.get('forum_id')
        forum = Forum.objects.filter(id=forum_id).first()
        forum_comment = Comment.objects.filter(forum=forum).order_by('-created_at')
        serializer = ViewForumCommentSerializer(forum_comment, many=True)
        try:
            data = {
                "data_type": "Forum Comment",
                "data": serializer.data,
            }
        except AttributeError:
            data = {
                "data_type": "Forum Comment",
                "data": [],
            }
        return Response(data, status=status.HTTP_200_OK)