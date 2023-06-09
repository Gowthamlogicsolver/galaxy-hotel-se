# Generated by Django 4.2 on 2023-04-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_rename_tblauthentication_hotelusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelusers',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hotelusers',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hotelusers',
            name='username',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
