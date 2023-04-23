from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import Category, SubCategory, Product
from apps.models.comments import CommentImages, Comment
from apps.models.product import ProductImages


# from django_elasticsearch_dsl import Document


class CategoryModelSerializer(ModelSerializer):
    def validate(self, data):
        if Category.objects.filter(name=data['name']).exists():
            raise ValidationError('This category is already taken')
        return data

    class Meta:
        model = Category
        exclude = ('slug',)


class SubCategoryModelSerializer(ModelSerializer):
    def validate(self, data):
        if SubCategory.objects.filter(name=data['name']).exists():
            raise ValidationError('This subcategory is already taken')
        return data

    class Meta:
        model = Category
        exclude = ('slug',)


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['images'] = ProductImageModelSerializer(instance.report_images.first()).data
        represent['subcategory_id'] = SubCategoryModelSerializer(instance.subcategory_id).data
        return represent

    class Meta:
        model = Product
        fields = '__all__'


class CommentImageModelSerializer(ModelSerializer):
    class Meta:
        model = CommentImages
        fields = '__all__'


class CommentModelSerializer(ModelSerializer):
    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['images'] = CommentImageModelSerializer(instance.report_images.first()).data
        return represent

    class Meta:
        model = Comment
        fields = '__all__'
