# Generated by Django 2.0.1 on 2018-01-16 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorizationManagement', '0003_auto_20180116_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='readers',
            new_name='resourcePermissions',
        ),
    ]
