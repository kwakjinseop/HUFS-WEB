# Generated by Django 3.2.2 on 2021-05-06 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Google',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('url', models.URLField(unique=True, verbose_name='URL')),
            ],
        ),
    ]