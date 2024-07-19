from rest_framework import serializers
from .models import BlogPost, User

class BlogPostSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = BlogPost
        fields =["id", "title", "content", "published_date"]

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields =["id", "gender", "password", "phone", "first", "email"]