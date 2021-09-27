from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename: str) -> str:
    return f'logo/{filename}'
# Create your models here.
class Store(models.Model):
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=127)
    lat = models.FloatField()
    lng = models.FloatField()
    slug = models.SlugField(max_length=255)
    logotype = models.ImageField(_("Image"),upload_to=upload_to,default='logo/default.png')