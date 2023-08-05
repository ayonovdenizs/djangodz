from django.db import models
from django.contrib import admin
from django.utils import timezone, html
from django.contrib.auth import get_user_model
# Create your models here

User = get_user_model()

class Advertisement(models.Model): # это класс-модель
    # он реализует таблицу Advertisement
    title = models.CharField("заголовок", max_length=128)
    text = models.TextField("описание")
    # author = models.CharField("автор", max_length=64)
    price = models.FloatField("цена")
    auction = models.BooleanField("торг", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField("Изображение", upload_to='media/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return f"title: {self.title}, text: {self.text}"