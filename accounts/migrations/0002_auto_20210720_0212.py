# Generated by Django 3.1.5 on 2021-07-19 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Address',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='line1',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='profile_pic'),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default='', max_length=255),
        ),
    ]
