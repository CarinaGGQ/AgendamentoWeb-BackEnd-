# Generated by Django 5.1.2 on 2024-12-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NAF', '0004_alter_serviço_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviço',
            name='nome',
            field=models.CharField(max_length=200),
        ),
    ]
