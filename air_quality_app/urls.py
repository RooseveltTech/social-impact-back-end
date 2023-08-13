from django.urls import path
from air_quality_app import views

air_quality = [
    path('v1/air-quality/', views.AirQualityAPIVIew.as_view()),
    path('v1/air-plants/', views.AirPlantsAPIVIew.as_view()),
    path('v1/blog/', views.Blogs.as_view()),
    path('v1/single_blog/', views.SingleBlogAPIView.as_view()),
    path('v1/like_blog/', views.LikeBlogAPIView.as_view()),
    path('v1/check_user/', views.CheckUserAPIView.as_view(), name=''),
    path('v1/forum_post/', views.ForumPostAPIView.as_view(), name=''),
    path('v1/get_forum_post/', views.GetAllForumPostAPIView.as_view(), name=''),
    path('v1/forum_comment/', views.ForumCommentAPIView.as_view(), name=''),
    path('v1/get_forum_comment/', views.GetAllForumCommentAPIView.as_view(), name=''),
]

urlpatterns = [
    *air_quality
]