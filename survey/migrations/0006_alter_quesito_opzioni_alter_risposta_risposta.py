# Generated by Django 4.1.4 on 2022-12-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "survey",
            "0005_alter_quesito_conclusione_alter_quesito_introduzione_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="quesito",
            name="opzioni",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="risposta",
            name="risposta",
            field=models.JSONField(blank=True, null=True),
        ),
    ]