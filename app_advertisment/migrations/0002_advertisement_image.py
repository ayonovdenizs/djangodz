# Generated by Django 4.0.4 on 2023-08-15 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='', verbose_name='image'),
            preserve_default=False,
        ),
    ]
