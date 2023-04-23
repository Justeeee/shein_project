from django.db.models import Model, CharField, IntegerField, ForeignKey, SET_NULL, CASCADE, TextField, BooleanField, \
    JSONField, ImageField, TextChoices
from django.utils.translation import gettext_lazy as _


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


    type = CharField(
        max_length=3,
        choices=Type.choices,
    )
    name = CharField(max_length=255)
    price = IntegerField(default=0)
    subcategory = ForeignKey('SubCategory', CASCADE)
    description = JSONField()
    quantity = IntegerField(default=1)
    # size = TODO add size
    # color = TODO add color
    # TODO add sold out
    exchangeable = BooleanField(default=False)


class ProductImage(Model):
    image = ImageField(upload_to='shops/images/')
    product = ForeignKey('apps.Product', CASCADE)
