# Generated by Django 5.1.2 on 2024-12-04 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NAF', '0007_remove_agendamento_codigo_transacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.CharField(default='DEFAULT VALUE', max_length=2000),
        ),
    ]