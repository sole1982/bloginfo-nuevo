<<<<<<< HEAD
# Generated by Django 4.2.7 on 2023-12-27 22:56
=======
# Generated by Django 4.2.7 on 2023-12-28 02:41
>>>>>>> 7ef31beeca663dd868f30bc117e598e2947c2bc6

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=150),
        ),
    ]
