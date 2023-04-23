from django.db.models import Model, CharField, IntegerField, ForeignKey, SET_NULL, CASCADE, TextField


class Product(Model):
    name = CharField(max_length=255)
    price = IntegerField(default=0)
    subcategory = ForeignKey('SubCategory',CASCADE)
    description = TextField()
    quantity = IntegerField(default=1)
    # color = TODO add color
    # TODO add sold out

