from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)

# Create your models here.


class Update(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to = upload_update_image, blank = True, null = True)
    updated = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    integer_field = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.content or ""
