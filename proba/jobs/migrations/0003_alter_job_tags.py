# Generated by Django 4.1.2 on 2022-11-06 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_rename_jobs_job_rename_tags_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='jobs.tag'),
        ),
    ]