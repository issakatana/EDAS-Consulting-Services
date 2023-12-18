from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib import admin
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, country, username, email, user_info, password=None, **extra_fields):
        if not country:
            raise ValueError('The country field is required')
        if not username:
            raise ValueError('The username field is required')
        if not email:
            raise ValueError('The email field is required')
        if not user_info:
            raise ValueError('The user information field is required')
        user = self.model(country=country, username=username, email=email, user_info = user_info, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, country, username, email, user_info, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(country, username, email,  user_info, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    country = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    user_info = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now_add=True)
   
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['country', 'username', 'user_info']
    
    def __str__(self):
        return self.email


class UserHelp(models.Model):
    full_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(null=True, blank=True, default='no message')
    newsletter = models.BooleanField(default=False)


@admin.register(UserHelp)
class UserHelpAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'phone_number', 'email', 'newsletter')
    list_filter = ('newsletter',)
    
           
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='pics', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(upload_to='pics', null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    user_name = models.CharField(max_length=200, default='Edas consultancy blog')

    def __str__(self):
        return self.title if self.title else f"Post {self.id}"