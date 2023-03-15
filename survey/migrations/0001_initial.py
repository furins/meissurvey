# Generated by Django 4.1.4 on 2022-12-11 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Quesito",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titolo", models.CharField(max_length=250)),
                (
                    "tipo",
                    models.IntegerField(
                        choices=[
                            (1, "Domanda aperta"),
                            (2, "Gradimento, scala da 1 a 5"),
                            (3, "Gradimento, scala da 1 a 6"),
                        ],
                        default=2,
                    ),
                ),
                ("opzioni", models.JSONField()),
            ],
            options={
                "verbose_name_plural": "quesiti",
            },
        ),
        migrations.CreateModel(
            name="Questionario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titolo", models.CharField(max_length=250)),
                ("url", models.SlugField()),
                ("inizio", models.DateTimeField()),
                ("fine", models.DateTimeField()),
            ],
            options={
                "verbose_name_plural": "questionari",
            },
        ),
        migrations.CreateModel(
            name="Risposte",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_risposta", models.DateTimeField(auto_created=True)),
                ("risposta", models.JSONField()),
                (
                    "quesito",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="survey.quesito"
                    ),
                ),
                (
                    "questionario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.questionario",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="quesito",
            name="questionario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="survey.questionario"
            ),
        ),
    ]
