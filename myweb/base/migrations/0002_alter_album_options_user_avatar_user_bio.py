# Generated by Django 5.0.6 on 2024-07-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.jpg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]