from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.template import loader

from core.serializers import RegistrationSerializer

# Create your views here.


class RegistrationAPIView(APIView):
    """Register a new user."""

    # permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        """Handle HTTP POST request."""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    
        

        
   

