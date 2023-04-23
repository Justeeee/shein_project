from django.db.models import Model, CharField, IntegerField, ForeignKey, SET_NULL, CASCADE, TextField, BooleanField, \
    JSONField, ImageField, TextChoices, SlugField, DecimalField, SmallIntegerField, DateTimeField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


def upload_directory_name(instance, filename):
    return f'products/{instance.product.id}/{filename}'


class Product(Model):
    class Type(TextChoices):
        UNDERWEAR = "UW", _("Underwear")
        HAT = "H", _("Hat")
        TSHIRT = "TSH", _("T-Shirt")
        SHOE = "SH", _("Shoe")
        PANTS = "P", _("Pants")

    class Size(TextChoices):
        X_SMALL = "XS", _("XS")
        SMALL = "S", _("S")
        MEDIUM = "M", _("M")
        LARGE = "L", _("L")
        X_LARGE = "XL", _("XL")
        XX_LARGE = "XXL", _("XXL")

    class Color(TextChoices):
        BLACK = "B", _("Black")
        WHITE = "W", _("White")
        GREEN = "G", _("Green")
        YELLOW = "Y", _("Yellow")
        RED = "R", _("Red")
        PURPLE = "P", _("Purple")

    type = CharField(
        max_length=3,
        choices=Type.choices,
    )
    color = CharField(
        max_length=1,
        choices=Color.choices,
        default=None
    )
    size = CharField(
        max_length=3,
        choices=Size.choices,
    )
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, blank=True)
    price = DecimalField(decimal_places=2, max_digits=9)
    subcategory = ForeignKey('SubCategory', CASCADE)
    detail = TextField()
    quantity = SmallIntegerField(default=1)
    discount = SmallIntegerField(default=0)
    information = JSONField(default=dict)
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)
    exchangeable = BooleanField(default=False)


    def __str__(self):
        return f'{self.name}'

    def stock(self):
        return 'In Stock' if self.quantity > 0 else 'Out of Stock'
    #
    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     self.slug = slugify(self.name)
    #     i = Product.objects.filter(slug=self.slug).count()
    #     while Product.objects.filter(slug=self.slug).exists():
    #         self.slug += f'{i}'
    #
    #     super().save(force_insert, force_update, using, update_fields)


class ProductImages(Model):
    product = ForeignKey('Product', CASCADE)
    image = ImageField(upload_to=upload_directory_name)

    def __str__(self):
        return f'{self.product.name} -> {self.image.name}'
