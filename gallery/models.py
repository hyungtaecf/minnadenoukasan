# GALLERY MODELS
from django.db import models

# Create your models here.
class GalleryImage(models.Model):
    title = models.CharField(max_length = 100, blank = True, null = True)
    image = models.ImageField(upload_to='gallery')
