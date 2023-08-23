# Generated by Django 4.2.4 on 2023-08-21 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0033_rename_regiao_ativa_suporte_regiao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suporte',
            name='equipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.equipe'),
        ),
        migrations.AlterField(
            model_name='suporte',
            name='regiao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suporte', to='dashboard.regional'),
        ),
    ]