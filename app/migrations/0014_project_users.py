# Generated by Django 3.2.9 on 2022-01-13 18:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0013_alter_userprofile_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Users',
            field=models.ManyToManyField(blank=True, related_name='Team', related_query_name='Team', to=settings.AUTH_USER_MODEL),
        ),
    ]
