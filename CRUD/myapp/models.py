from django.db import models

# Create your models here.
class Information(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name