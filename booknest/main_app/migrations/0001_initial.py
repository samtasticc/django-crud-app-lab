# Generated by Django 5.1.6 on 2025-02-20 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=5000)),
            ],
        ),
    ]
