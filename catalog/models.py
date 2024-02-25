from django.db import models

class Product(models.Model):

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
