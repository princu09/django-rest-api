# Generated by Django 4.1 on 2022-08-28 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tour", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tour",
            name="desc",
        ),
    ]
