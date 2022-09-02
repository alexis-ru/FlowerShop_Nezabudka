from django.db import models


class Shop(models.Model):
    title = models.CharField('Наименование', max_length=50)
    typeFlower = models.CharField('Тип цветка', max_length=250)
    description = models.TextField('Описание')
    date = models.DateTimeField('Дата покупки')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/shop/{self.id}'

    class Meta:
        verbose_name = 'Цветочный магазин'
        verbose_name_plural = 'Цветочные магазины'
