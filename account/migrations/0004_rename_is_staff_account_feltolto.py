# Generated by Django 4.2.3 on 2023-08-07 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_username_account_felhasznalonev'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_staff',
            new_name='feltolto',
        ),
    ]
