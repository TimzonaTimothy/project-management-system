# Generated by Django 4.2.4 on 2023-09-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_auto_20180403_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='register.userprofile'),
        ),
    ]
