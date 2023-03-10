from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


