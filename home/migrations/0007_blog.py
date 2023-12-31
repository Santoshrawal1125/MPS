# Generated by Django 4.2.5 on 2023-09-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='media')),
                ('body', models.TextField()),
            ],
        ),
    ]
