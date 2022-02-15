from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    image = models.ImageField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    text = models.TextField(blank=False, null=False)
