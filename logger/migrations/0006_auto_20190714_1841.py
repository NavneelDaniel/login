# Generated by Django 2.0.7 on 2019-07-14 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0005_auto_20190714_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='flatno',
            new_name='Flatno',
        ),
    ]
