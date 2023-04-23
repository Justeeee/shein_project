from django.db.models import Model, ForeignKey, CharField, TextField, SmallIntegerField, DateTimeField, CASCADE, \
    ImageField


def upload_directory_name(instance, filename):
    return f'comments/{instance.comment.id}/{filename}'


class Comment(Model):
    product = ForeignKey('Product', CASCADE)
    headline = CharField(max_length=255)
    text = TextField()
    author = ForeignKey('users.User', CASCADE)
    rate = SmallIntegerField(default=0)
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)


class CommentsImages(Model):
    comment = ForeignKey('Comment', CASCADE)
    image = ImageField(upload_to=upload_directory_name)

    def __str__(self):
        return f'{self.comment.headline} -> {self.image.name}'
