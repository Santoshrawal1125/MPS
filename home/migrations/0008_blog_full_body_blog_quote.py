# Generated by Django 4.2.5 on 2023-09-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='full_body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='quote',
            field=models.TextField(blank=True),
        ),
    ]
