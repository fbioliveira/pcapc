# Generated by Django 4.2.4 on 2023-08-17 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_remove_dashboard_equipes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loja',
            name='status_concluida',
        ),
        migrations.AddField(
            model_name='loja',
            name='concluida',
            field=models.BooleanField(default=False),
        ),
    ]
