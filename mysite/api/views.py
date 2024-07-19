from django.shortcuts import render
from .models import BlogPost, User
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import BlogPostSerializer, UserSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class BlogPostListCreate(generics.ListCreateAPIView): 
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer 

    def delete (self, request, *args, **kwargs):
        return Response (status = status.HTTP_204_NO_CONTENT)

class BlogPostRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView): 
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer 
    lookup_field = "pk"

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk" 

# Can create from an API only admits post
class UserCreateView(APIView):
    def post(self, request): 
        data = request.data.get('results')[0]

        user_data = {
            "gender": data["gender"],
            "first": data["name"]["first"],
            "email": data["email"],
            "password": data["login"]["password"],
            "phone": data["phone"]
        }

        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class UserView(APIView): 
    def get (self, request, pk=None): 
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data.get('results')[0]  # Acceder al primer diccionario dentro de 'results'

        # Reorganizar el JSON según los campos del serializador
        user_data = {
            "gender": data["gender"],
            "first": data["name"]["first"],
            "email": data["email"],
            "password": data["login"]["password"],
            "phone": data["phone"]
        }

        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        data = request.data.get('results')[0]

        user_data = {
            "gender": data["gender"],
            "first": data["name"]["first"],
            "email": data["email"],
            "password": data["login"]["password"],
            "phone": data["phone"]
        }

        serializer = UserSerializer(user, data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class BlogPostList(APIView):
    def get(self, request, format = None):
        title = request.query_params.get('title', "")

        if title: 
            blog_post = BlogPost.objects.filter(title__icontains=title)
        else: 
            blog_post = BlogPost.objects.all()  

        serializer = BlogPostSerializer(blog_post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
