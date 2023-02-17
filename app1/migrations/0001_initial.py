# Generated by Django 4.1.4 on 2023-02-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('area', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
