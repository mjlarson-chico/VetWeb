# Generated by Django 3.0.4 on 2020-05-05 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200505_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resources',
            name='has_tutorials',
        ),
        migrations.DeleteModel(
            name='Tutorials',
        ),
    ]
