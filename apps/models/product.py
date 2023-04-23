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
    )
    name = CharField(max_length=255)
    price = IntegerField(default=0)
    subcategory = ForeignKey('SubCategory', CASCADE)
    description = JSONField()
    quantity = IntegerField(default=1)
    # size = TODO add size
    # TODO add sold out
    exchangeable = BooleanField(default=False)


class ProductImage(Model):
    image = ImageField(upload_to='shops/images/')
    product = ForeignKey('apps.Product', CASCADE)
