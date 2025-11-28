from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    date = models.DateField()
    amount = models.FloatField()
    status = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    