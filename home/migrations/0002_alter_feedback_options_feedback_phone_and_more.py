# Generated by Django 4.2.4 on 2023-08-24 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'фидбэк', 'verbose_name_plural': 'Фидбэк'},
        ),
        migrations.AddField(
            model_name='feedback',
            name='phone',
            field=models.CharField(max_length=50, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='is_check',
            field=models.BooleanField(default=False, verbose_name='Просмотрено?'),
        ),
    ]
