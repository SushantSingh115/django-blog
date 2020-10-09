from django.contrib.auth.models import User
from .serializers import PostsSerializer, UserSerializer, \
    ProfileUpdateSerializer,UserPostsSerializer, PostList1, ProfileSerializer
from rest_framework import generics
from blog.models import Post
from users.models import Profile
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly

class PostsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('author','title')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer



class UserProfileUpdate(generics.UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = None

    def get_queryset(self):
        user = self.request.user
        user = User.objects.filter(id=user.id)
        return user


class UserPostsList(generics.ListCreateAPIView):
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        posts = Post.objects.filter(author=user)
        return posts

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostsListViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostList1
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        return Response("Api to register user")


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def list(self, request, *args, **kwargs):
        return Response("Api to Update user")