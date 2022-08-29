from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    user=models.CharField(max_length=50)
    image = models.ImageField(upload_to="postimage",null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title