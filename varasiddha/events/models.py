from django.db import models

# Create your models here.

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('program', 'Program'),
        ('festival', 'Festival'),
    ]

    name = models.CharField(max_length=100)
    date = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.category}"
