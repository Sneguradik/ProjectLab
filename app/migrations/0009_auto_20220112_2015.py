# Generated by Django 3.2.9 on 2022-01-12 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220111_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='Project',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Project',
            field=models.ManyToManyField(to='app.Project'),
        ),
    ]
