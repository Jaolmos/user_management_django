# Generated by Django 3.2.7 on 2021-10-01 05:15

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211001_0648'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
