# Generated by Django 4.2.7 on 2023-12-27 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
