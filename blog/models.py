from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from six import python_2_unicode_compatible
from slugify import slugify

# Create your models here.

# TODO: Create "Tag" class and link it by Foreign Key

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=20)
    text = RichTextUploadingField(verbose_name="Content")
    image = models.ImageField(upload_to='blog/post_image', verbose_name="Main Picture", null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering= ['-publish_date']
