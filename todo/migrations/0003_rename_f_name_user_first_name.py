# Generated by Django 3.2.6 on 2021-09-07 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_first_name_user_f_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='f_name',
            new_name='first_name',
        ),
    ]