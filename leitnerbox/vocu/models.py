from django.db import models

# Create your models here.

class Words(models.Model):
    id = models.IntegerField(primary_key=True)
    english = models.CharField(max_length=240)
    spanish = models.CharField(max_length=240)
    info = models.TextField()
    box = models.IntegerField(default=0)

    def _str_(self):
        return self.spanish
