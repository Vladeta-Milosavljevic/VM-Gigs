# Generated by Django 4.1.2 on 2023-02-03 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_alter_job_email_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='job_logo/'),
        ),
    ]
