# Generated by Django 3.0.3 on 2020-03-02 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filebox', '0003_auto_20200302_0542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='author',
            new_name='uploaded_by',
        ),
    ]
