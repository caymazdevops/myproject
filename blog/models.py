from django.db import models # type: ignore

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title

