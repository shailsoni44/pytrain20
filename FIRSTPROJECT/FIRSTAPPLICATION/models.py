from django.db import models


# Create your models here.
class Information(models.Model):
    ID = models.CharField(primary_key=True, max_length=2, unique=True)
    Name = models.CharField(max_length = 25)
    Contact = models.CharField(max_length = 15)
    Address = models.CharField(max_length = 50)
    
    class Meta:
        verbose_name_plural = "Information"

    def __str__(self):
        return self.Name