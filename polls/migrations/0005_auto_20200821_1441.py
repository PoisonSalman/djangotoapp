# Generated by Django 2.1.5 on 2020-08-21 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200821_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='question',
            name='image5',
        ),
        migrations.AddField(
            model_name='choice',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
