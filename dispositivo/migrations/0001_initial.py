# Generated by Django 5.0.3 on 2024-03-11 23:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
