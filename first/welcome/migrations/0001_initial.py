# Generated by Django 5.1.6 on 2025-02-17 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pages',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
    ]
