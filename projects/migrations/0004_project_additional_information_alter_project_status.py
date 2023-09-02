# Generated by Django 4.2.4 on 2023-09-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20180403_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='additional_information',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('1', 'Active'), ('2', 'Completed'), ('3', 'On Hold')], default=1, max_length=7),
        ),
    ]
