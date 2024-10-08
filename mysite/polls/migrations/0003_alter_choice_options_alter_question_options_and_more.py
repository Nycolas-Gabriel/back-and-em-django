# Generated by Django 5.1.1 on 2024-10-07 02:29

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_question_active"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="choice",
            options={"verbose_name": "Opção", "verbose_name_plural": "Opções"},
        ),
        migrations.AlterModelOptions(
            name="question",
            options={"verbose_name": "Questão", "verbose_name_plural": "Questões"},
        ),
        migrations.RemoveField(
            model_name="choice",
            name="votes",
        ),
        migrations.AddField(
            model_name="choice",
            name="vote",
            field=models.IntegerField(default=0, verbose_name="Votos"),
        ),
        migrations.AlterField(
            model_name="choice",
            name="choice_text",
            field=models.CharField(max_length=200, verbose_name="Descrição"),
        ),
        migrations.AlterField(
            model_name="choice",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="polls.question",
                verbose_name="Questão",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="active",
            field=models.BooleanField(default=True, verbose_name="Ativo"),
        ),
        migrations.AlterField(
            model_name="question",
            name="pub_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Data da publicação"
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="question_text",
            field=models.CharField(max_length=200, verbose_name="Texto da questão"),
        ),
    ]
