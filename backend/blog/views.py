from .models import Category,Tag,Post,Comment
from .serializers import TagSerializer,PostSerializer,CommentSerializer,CategorySerializer
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class PostCreateViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostCreateSerializer

