# Generated by Django 4.2.1 on 2023-05-13 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buds', '0012_delete_daily_delete_monthly'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monthly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.IntegerField()),
                ('utilites', models.IntegerField()),
                ('personal_care', models.IntegerField()),
                ('communication', models.IntegerField()),
                ('health', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.IntegerField()),
                ('transport', models.IntegerField()),
                ('entertain', models.IntegerField()),
                ('stationary', models.IntegerField()),
                ('misc', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
