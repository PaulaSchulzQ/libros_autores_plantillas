# Generated by Django 3.1.7 on 2021-02-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros_autores_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notas',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]