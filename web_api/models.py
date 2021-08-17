from django.db import models

# Create your models here.
class Userprofile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    have_account = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Trial(models.Model):
    name1 = models.CharField(max_length=100)

    def __str__(self):
        return self.name1