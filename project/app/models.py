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

class Saves(models.Model):
    user_id = models.IntegerField()
    user_saves = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'user_saves')

    def __str__(self):
        return f"Пользователь {self.user_id} сохранил новость {self.user_saves.main}"





