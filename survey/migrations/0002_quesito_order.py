# Generated by Django 4.1.4 on 2022-12-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="quesito",
            name="order",
            field=models.PositiveIntegerField(
                db_index=True, default=0, editable=False, verbose_name="order"
            ),
            preserve_default=False,
        ),
    ]
