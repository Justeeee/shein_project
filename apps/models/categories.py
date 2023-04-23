from django.db.models import CharField, SlugField, ForeignKey, CASCADE
from django.db.models import Model, DateTimeField
from django.utils.text import slugify


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, blank=True)



    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    name = CharField(max_length=255)
    parent = ForeignKey('Category', CASCADE, related_name='subcategory')
    slug = SlugField(max_length=255, unique=True, blank=True)
    verbose_name_plural = 'SubCategories'




    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while SubCategory.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name
