# Generated by Django 5.1.2 on 2024-12-01 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NAF', '0005_alter_serviço_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='Feedback',
        ),
    ]
