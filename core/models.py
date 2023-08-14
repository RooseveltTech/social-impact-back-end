from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import check_password
import uuid
import json, os

# Create your model(s) here.
class BaseModel(models.Model):
    """Base model for reuse.
    Args:
        models (Model): Django's model class.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(_('date created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, BaseModel):
    """User model."""

    CHANNEL = [
        ("WEB", "WEB"),
        ("MOBILE", "MOBILE"),
    ]

    username = None
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, )
    first_name = models.CharField(max_length=255, blank=False, null=True)
    last_name = models.CharField(max_length=255, blank=False, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    with open(os.path.dirname(__file__)+'/countries_data.json') as f:
        countries_json = json.load(f)
        COUNTRIES_ISD_CODES = [(str(country["name"]), str(country["name"])) for country in countries_json]
        COUNTRIES_PHONE_CODES = [(str(country["name"]), str(country["dialling_code"])) for country in countries_json]
    country = models.CharField(max_length=255,choices=COUNTRIES_ISD_CODES)
    channel = models.CharField(max_length=200, choices=CHANNEL, default="WEB")
    user_is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return str(self.email)

    class Meta:
        ordering = ['-created_at']
        # verbose_name = 'USER PROFILE'
        # verbose_name_plural = 'USER PROFILES'

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def user_exist(cls, email):
        try:
            user = cls.objects.get(email=email)
        except cls.DoesNotExist:
            return None
        return user
    
    def username_exist(cls, username):
        try:
            username = cls.objects.get(username=username)
        except cls.DoesNotExist:
            return None
        return username
    
    