# Generated by Django 5.0.6 on 2024-06-24 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('cover', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
            ],
        ),
    ]
