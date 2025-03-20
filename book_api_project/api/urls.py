# api/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, BookListCreate, BookRetrieveUpdateDestroy,
    PublisherListCreate, PublisherRetrieveUpdateDestroy
)

urlpatterns = [
    # usrls for user registration and authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # userls for books
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-detail'),
    
    # usrls for publishers
    path('publishers/', PublisherListCreate.as_view(), name='publisher-list-create'),
    path('publishers/<int:pk>/', PublisherRetrieveUpdateDestroy.as_view(), name='publisher-detail'),
]