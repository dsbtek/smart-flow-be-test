# Generated by Django 4.0.6 on 2022-07-18 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
