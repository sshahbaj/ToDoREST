# Generated by Django 2.1 on 2018-08-16 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_todoitem_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='item',
            new_name='subject',
        ),
    ]
