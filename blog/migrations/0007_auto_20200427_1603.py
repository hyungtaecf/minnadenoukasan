# Generated by Django 3.0.3 on 2020-04-27 19:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200427_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
