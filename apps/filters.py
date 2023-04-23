from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from apps.models import Product


class ProductFilter(FilterSet):
    hash_tags = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ('type', 'size', 'color', 'name', 'subcategory')
