# Generated by Django 4.2.9 on 2024-01-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuarios",
            fields=[
                ("id_usuario", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.TextField()),
                ("idade", models.IntegerField()),
            ],
        ),
    ]
