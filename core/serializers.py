from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, exceptions
from rest_framework.exceptions import ValidationError


User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'city', 'country', 'ip_address', 'air_city', 'password')
        # extra_kwargs = {
        #     'email': {'required': True},
        #     'first_name': {'required': True, 'allow_null': False},
        #     'last_name': {'required': True, 'allow_null': False},
        #     'country_code': {'required': False, 'allow_null': False},
        #     'phone_number': {'required': False, 'allow_null': False},
        #     'city': {'required': True, 'allow_null': False},
        #     'street': {'required': False, 'allow_null': False},
        #     'country': {'required': True, 'allow_null': False},
        #     'password': {'write_only': True, 'allow_null': False},
        #     'street': {'required': False, 'allow_null': False},
        # }
    def validate(self, value):
        value['password'] = make_password(value['password'])
        return value
    
class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs[self.username_field].lower()

        authenticate_kwargs = {
            self.username_field: email,
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
            authenticate_kwargs['email'] = authenticate_kwargs['email'].lower()
        except KeyError:
            pass
        '''
            Checking if the user exists by getting the email(username field) from authentication_kwargs.
            If the user exists we check if the user account is active.
            If the user account is not active we raise the exception and pass the message.
            Thus stopping the user from getting authenticated altogether.

            And if the user does not exist at all we raise an exception with a different error message.
            Thus stopping the execution right there.
        '''
        try:
            user = User.objects.get(email=authenticate_kwargs['email'])
            if user.is_active is False:
                self.error_messages['error'] = (
                    'account disabled. please contact admin'
                )
                raise exceptions.AuthenticationFailed(
                    self.error_messages['error']
                )

        except User.DoesNotExist:
            self.error_messages['no_active_account'] = (
                'account does not exist')
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
            )
        authenticate_kwargs['email'] = user.email.lower()

        self.user = authenticate(email=user.email.lower(), password = authenticate_kwargs['password'])
        if self.user is None:
            self.error_messages['no_active_account'] = (
                'password is incorrect. please enter a correct password')
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
            )
        print(self.user.is_active)
        
        return super().validate(attrs)
        
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer



