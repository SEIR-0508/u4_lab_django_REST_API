# Generated by Django 4.2.3 on 2023-07-18 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vct_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='players', to='vct_app.team'),
        ),
    ]
