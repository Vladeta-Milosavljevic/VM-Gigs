# Generated by Django 4.1.2 on 2022-11-15 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_alter_job_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
