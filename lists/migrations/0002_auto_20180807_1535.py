# Generated by Django 2.1 on 2018-08-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='id',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='auto_increment_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
