from django.shortcuts import render

from rest_framework import generics

# Create your views here.
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializer import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

