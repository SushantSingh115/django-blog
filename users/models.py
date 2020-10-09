from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='Profile_Pics/default.jpg', upload_to='Profile_Pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        im = Image.open(self.img.path)
        if im.height>300 or im.width>300:
            output_size=(300,300)
            im.thumbnail(output_size)
            im.save(self.img.path)


