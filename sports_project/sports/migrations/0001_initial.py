# Generated by Django 4.2.7 on 2023-11-17 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('division', models.CharField(max_length=100)),
                ('wins', models.CharField(max_length=100)),
                ('losses', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('injured', models.BooleanField(default=False)),
                ('number', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='sports.team')),
            ],
        ),
    ]
