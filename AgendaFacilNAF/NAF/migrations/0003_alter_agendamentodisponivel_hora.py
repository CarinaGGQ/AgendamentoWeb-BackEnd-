# Generated by Django 5.1.2 on 2024-11-17 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NAF', '0002_remove_professor_usuario_delete_aluno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamentodisponivel',
            name='hora',
            field=models.CharField(choices=[('9h', '9h às 10h'), ('10h', '10h às 11h'), ('11h', '11h às 12h'), ('12h', '12h às 13h'), ('13h', '13h às 14h'), ('14h', '14h às 15h'), ('15h', '15h às 16h'), ('16h', '16h às 17h'), ('17h', '17h às 18h')], max_length=5),
        ),
    ]
