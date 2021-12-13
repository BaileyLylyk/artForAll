from django.db import models

# Create your models here.
class GalleryPost(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank =True, null=True)
    artist      = models.CharField(max_length=120)
    featured    = models.BooleanField(default= False)
    image       = models.ImageField(null = True, blank = True, upload_to = "static/img/")