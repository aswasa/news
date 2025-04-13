from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    name=models.CharField(max_length=64)
    date=models.CharField(max_length=8)

    def __str__(self):
        return self.name

class News(models.Model):
    main=models.TextField(max_length=64)
    text=models.TextField()
    category=models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    daten=models.CharField(max_length=8)

    def __str__(self):
        return self.main

