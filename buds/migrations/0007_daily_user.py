# Generated by Django 4.2.1 on 2023-05-13 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buds', '0006_remove_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buds.user'),
        ),
    ]
