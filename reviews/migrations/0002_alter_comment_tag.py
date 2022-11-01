# Generated by Django 3.2.13 on 2022-11-01 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='tag',
            field=models.CharField(choices=[('midnight snack', '야메추'), ('dinner', '저메추'), ('lunch', '점메추'), ('morning', '아메추')], max_length=32, verbose_name='태그명'),
        ),
    ]