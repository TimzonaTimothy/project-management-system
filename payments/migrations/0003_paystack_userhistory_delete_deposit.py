# Generated by Django 4.2.4 on 2023-09-02 15:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_deposit_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paystack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=1000000)),
                ('email', models.EmailField(blank=True, max_length=3000, null=True)),
                ('reference', models.CharField(max_length=200)),
                ('generated', models.DateTimeField(default=django.utils.timezone.now)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-generated',),
            },
        ),
        migrations.CreateModel(
            name='Userhistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=40, null=True)),
                ('amount', models.CharField(blank=True, max_length=30, null=True)),
                ('transaction', models.CharField(blank=True, choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')], max_length=20, null=True)),
                ('confirm', models.BooleanField(default=False)),
                ('date_created', models.DateField()),
                ('paystack', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.paystack')),
            ],
            options={
                'verbose_name_plural': 'User Histories',
                'ordering': ('-date_created',),
            },
        ),
        migrations.DeleteModel(
            name='Deposit',
        ),
    ]
