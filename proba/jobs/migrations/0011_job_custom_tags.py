# Generated by Django 4.1.2 on 2022-11-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_alter_job_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='custom_tags',
            field=models.CharField(default=55, max_length=100),
            preserve_default=False,
        ),
    ]