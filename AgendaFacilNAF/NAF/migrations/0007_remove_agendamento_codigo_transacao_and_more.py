# Generated by Django 5.1.2 on 2024-12-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NAF', '0006_remove_agendamento_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='codigo_transacao',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='finalizado',
        ),
        migrations.AddField(
            model_name='feedback',
            name='feedback',
            field=models.CharField(default='Sem Feedback', max_length=2000),
            preserve_default=False,
        ),
    ]
