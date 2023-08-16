from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from django.shortcuts import render
from django.template import loader
from django.contrib.auth import get_user_model
from air_quality_app.apis.call_api import AirQuality

from core.serializers import RegistrationSerializer

from drf_yasg.utils import swagger_auto_schema
# Create your views here.

User = get_user_model()

class RegistrationAPIView(APIView):
    """Register a new user."""

    # permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    @swagger_auto_schema(request_body=RegistrationSerializer)
    def post(self, request):
        """Handle HTTP POST request."""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    
class CheckEmailAPIView(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        user = User.objects.filter(email=email)
        if user.exists():
            return Response(
                {
                    "exist": True
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "exist": False
                },
                status=status.HTTP_200_OK
            )
        

        
   

