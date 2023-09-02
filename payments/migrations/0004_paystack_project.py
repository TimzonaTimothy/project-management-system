# Generated by Django 4.2.4 on 2023-09-02 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_project_id_alter_project_status_receipt'),
        ('payments', '0003_paystack_userhistory_delete_deposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='paystack',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]
