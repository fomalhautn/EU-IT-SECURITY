from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264, unique=True)
    text = models.TextField()

    def __str__(self):
        return self.name