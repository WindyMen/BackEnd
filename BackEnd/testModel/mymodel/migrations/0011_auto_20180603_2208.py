# Generated by Django 2.0.3 on 2018-06-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0010_auto_20180527_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
