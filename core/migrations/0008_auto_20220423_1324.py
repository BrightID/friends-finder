# Generated by Django 3.1.7 on 2022-04-23 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220322_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmediavariation',
            old_name='bright_id_app_name',
            new_name='bright_id_app_id',
        ),
    ]
