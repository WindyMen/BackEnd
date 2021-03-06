# Generated by Django 2.0.3 on 2018-06-06 13:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0013_auto_20180603_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='endTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='room/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='room/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='room/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='room/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='room/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo6',
            field=models.ImageField(blank=True, null=True, upload_to='room/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo7',
            field=models.ImageField(blank=True, null=True, upload_to='room/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo8',
            field=models.ImageField(blank=True, null=True, upload_to='room/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo9',
            field=models.ImageField(blank=True, null=True, upload_to='room/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='specificAddress',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='startTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
