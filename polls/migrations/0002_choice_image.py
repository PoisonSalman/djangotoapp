# Generated by Django 2.1.5 on 2020-08-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]
                
    operations = [
        migrations.AddField(
            model_name='choice',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
