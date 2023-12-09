from django.db import models
from django.utils.text import slugify

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from .fields import OrderField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=150)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.name)

        if update_fields is not None and "name" in update_fields:
            update_fields = {'slug'}.union(update_fields)

        return super().save(force_insert, force_update, using, update_fields)


class Manga(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='mangas')
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=250)
    title = models.CharField(max_length=250)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)

        if update_fields is not None and "title" in update_fields:
            update_fields = {'slug'}.union(update_fields)

        return super().save(force_insert, force_update, using, update_fields)


class Content(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='contents')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': ('season', 'movie', 'episode')})
    object_id = models.PositiveIntegerField()
    order = OrderField(for_fields=['manga'])

    class Meta:
        ordering = ['order']
        indexes = [
            models.Index(fields=['order'])
        ]


class BaseVideo(models.Model):
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=250)
    title = models.CharField(max_length=250)

    poster = models.ImageField(upload_to='mangas/posters')
    video = models.FileField(upload_to='mangas/videos')

    type = models.CharField(default='video/mp4', max_length=20)
    duration = models.CharField(null=True, blank=True, max_length=10)
    fps = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)

        if update_fields is not None and "title" in update_fields:
            update_fields = {'slug'}.union(update_fields)

        return super().save(force_insert, force_update, using, update_fields)

    def get_ratio(self):
        if self.width and self.height:
            return self.width / self.height
        return 16/9

    class Meta:
        abstract = True


class Season(models.Model):
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=250)
    title = models.CharField(max_length=250)

    def model_name(self):
        return self._meta.model_name


class Movie(BaseVideo):
    def model_name(self):
        return self._meta.model_name


class Episode(BaseVideo):
    season = models.ForeignKey(Season, null=True, blank=True, related_name='episodes', on_delete=models.CASCADE)

    def model_name(self):
        return self._meta.model_name
