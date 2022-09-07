from django.utils import timezone
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_images/')
    

    class Meta:
        verbose_name = ("Posts")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
