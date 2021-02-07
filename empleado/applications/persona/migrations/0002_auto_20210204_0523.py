# Generated by Django 3.1.5 on 2021-02-04 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(blank=True, to='persona.Habilidades'),
        ),
    ]
