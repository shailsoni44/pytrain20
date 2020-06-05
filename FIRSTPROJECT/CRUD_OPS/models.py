from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(max_length = 25)
    email = models.EmailField(max_length = 50, unique = True)
    Repeat_email = models.CharField(max_length = 50,)
    password = models.CharField(max_length = 15,)
    re_password = models.CharField(max_length = 15,)

    class Meta:
        verbose_name_plural = "Register"

    def __str__(self):
        return self.name