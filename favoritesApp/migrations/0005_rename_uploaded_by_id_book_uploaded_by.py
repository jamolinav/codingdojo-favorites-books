# Generated by Django 3.2.3 on 2021-05-21 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favoritesApp', '0004_auto_20210521_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='uploaded_by_id',
            new_name='uploaded_by',
        ),
    ]
