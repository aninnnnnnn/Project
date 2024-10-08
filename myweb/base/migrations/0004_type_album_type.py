# Generated by Django 5.0.6 on 2024-08-01 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='albums', to='base.type'),
        ),
    ]
