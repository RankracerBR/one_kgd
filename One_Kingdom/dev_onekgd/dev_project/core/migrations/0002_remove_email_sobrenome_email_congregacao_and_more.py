# Generated by Django 4.1.5 on 2023-05-31 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='sobrenome',
        ),
        migrations.AddField(
            model_name='email',
            name='congregacao',
            field=models.CharField(default='Congregacao', max_length=100),
        ),
        migrations.AlterField(
            model_name='email',
            name='nome',
            field=models.CharField(default='Nome', max_length=100),
        ),
    ]
