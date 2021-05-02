from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/category', blank=True)

    class Meta():
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name
    
