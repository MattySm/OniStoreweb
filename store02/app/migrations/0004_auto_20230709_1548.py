# Generated by Django 3.1.2 on 2023-07-09 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_productos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
