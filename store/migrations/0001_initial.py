# Generated by Django 3.2.5 on 2021-09-25 21:03

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=127)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('slug', models.SlugField(max_length=255)),
                ('logotype', models.ImageField(default='logo/default.png', upload_to=store.models.upload_to, verbose_name='Image')),
            ],
        ),
    ]
