from django.db import models


# Create your models here.

class Minorsubjects(models.Model):
    name = models.CharField(max_length=100)
    durations = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'Minor Subject'

    def __str__(self):
        return self.name
