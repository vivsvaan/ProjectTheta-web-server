# Generated by Django 3.1 on 2020-08-10 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiSecretToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=50)),
                ('is_web_client', models.BooleanField(default=False)),
                ('api_key', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
