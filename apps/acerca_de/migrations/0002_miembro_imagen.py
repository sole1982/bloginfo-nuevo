# Generated by Django 4.2.7 on 2023-12-28 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acerca_de', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='imagen',
            field=models.ImageField(blank=True, default='usuario/user-default.png', null=True, upload_to='media'),
        ),
    ]