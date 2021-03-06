# Generated by Django 2.1 on 2018-08-21 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_todoitem_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('pub_date', models.DateField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.Blog')),
            ],
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
