# api/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Book, Publisher
from .serializers import UserSerializer, BookSerializer, PublisherSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# User Registration View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": UserSerializer(user).data,
                "message": "User registered successfully",
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Book Views
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

# Publisher Views
class PublisherListCreate(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (permissions.IsAuthenticated,)

class PublisherRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (permissions.IsAuthenticated,)