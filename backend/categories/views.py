from rest_framework import generics
from categories.serializers import CategorySerializer
from categories.models import Category

# Create your views here.
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
