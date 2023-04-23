from django.http import HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.openapi import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from apps.filters import ProductFilter
from apps.models import Category, SubCategory
from apps.models.product import ProductImages, Product
from apps.serializers import CategoryModelSerializer, ProductImageModelSerializer, ProductModelSerializer, \
    SubCategoryModelSerializer


# def index(request):
#     return HttpResponse(1)


# Create your views here.
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.order_by('-created_at')
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'

class SubCategoryModelViewSet(ModelViewSet):
    queryset = SubCategory.objects.order_by('-created_at')
    serializer_class = SubCategoryModelSerializer
    lookup_field = 'slug'


class ProductImageAPIView(GenericAPIView):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImageModelSerializer
    parser_classes = (MultiPartParser,)

    def get(self, request):
        images = self.queryset.all()
        serializer = self.serializer_class(images, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.order_by('-created_at')
    serializer_class = ProductModelSerializer
    lookup_url_kwarg = 'id'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'title']
    filterset_class = ProductFilter


