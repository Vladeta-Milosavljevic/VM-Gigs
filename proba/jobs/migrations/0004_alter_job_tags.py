# Generated by Django 4.1.2 on 2022-11-06 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='tags',
            field=models.ManyToManyField(blank=True, to='jobs.tag'),
        ),
    ]