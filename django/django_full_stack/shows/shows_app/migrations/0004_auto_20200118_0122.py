# Generated by Django 2.2 on 2020-01-18 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows_app', '0003_auto_20200116_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='desc',
            field=models.DateField(),
        ),
    ]