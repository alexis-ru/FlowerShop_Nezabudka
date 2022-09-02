from django.db import models


class Address(models.Model):
    titles = models.CharField('Наименование', max_length=100)
    places = models.TextField('Адрес магазина')
    description = models.CharField('Ближайшее метро', max_length=100)

    def __str__(self):
        return self.titles
