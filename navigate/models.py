from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.name
