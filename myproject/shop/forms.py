from .models import Shop
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ['title', 'typeFlower', 'description', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Наименовние"
            }),
            "typeFlower": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Тип цветка"
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Описание"
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата продажи"
            })
        }
