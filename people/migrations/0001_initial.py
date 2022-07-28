# Generated by Django 4.0.6 on 2022-07-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256)),
                ('birth_date', models.DateField(null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]