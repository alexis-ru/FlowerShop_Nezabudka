# Generated by Django 3.2.15 on 2022-09-02 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_address_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='test',
        ),
    ]
