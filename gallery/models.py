from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=250)
    description1 = models.TextField()
    description2 = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title