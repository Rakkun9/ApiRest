from django.urls import path
from . import views 

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-view-create'),
    path('blogposts/<int:pk>/', views.BlogPostRetriveUpdateDestroy.as_view(), name='update',),
    path('users/<int:pk>/', views.UserRetriveUpdateDestroy.as_view(), name="user-list"),
    path('users/', views.UserListCreate.as_view(), name='user-view-create'),
    path('usersHi', views.UserCreateView.as_view(), name = 'user-create'),
    
    path('usersHola/', views.UserView.as_view(), name='user-list-create'),
    path('usersHola/<int:pk>/', views.UserView.as_view(), name='user-detail-update-delete'),
]
