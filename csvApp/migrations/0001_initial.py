# Generated by Django 3.0.6 on 2020-06-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_field', models.CharField(blank=True, max_length=200)),
                ('modeltype', models.CharField(blank=True, max_length=20)),
                ('modelName', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
