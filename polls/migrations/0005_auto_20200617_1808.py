# Generated by Django 3.0.7 on 2020-06-17 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200617_1751'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='choice',
            table='choice',
        ),
        migrations.AlterModelTable(
            name='question',
            table='question',
        ),
    ]
