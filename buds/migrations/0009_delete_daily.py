# Generated by Django 4.2.1 on 2023-05-13 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buds', '0008_alter_daily_user_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Daily',
        ),
    ]
