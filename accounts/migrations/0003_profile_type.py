# Generated by Django 3.1.5 on 2021-07-19 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210720_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('1', 'Doctor'), ('2', 'Patient')], default='', max_length=255),
        ),
    ]
