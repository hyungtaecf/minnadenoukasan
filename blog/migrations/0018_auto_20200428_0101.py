# Generated by Django 3.0.3 on 2020-04-28 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200428_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/post_image'),
        ),
    ]
