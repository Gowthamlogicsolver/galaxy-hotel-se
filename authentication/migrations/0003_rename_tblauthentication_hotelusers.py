# Generated by Django 4.2 on 2023-04-11 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_tblauthentication_delete_tbl_authentiction'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TblAuthentication',
            new_name='hotelusers',
        ),
    ]
