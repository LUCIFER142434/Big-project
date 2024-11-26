# Generated by Django 5.0.7 on 2024-11-21 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='HeaderEnd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_top', models.CharField(max_length=30)),
                ('text_big', models.CharField(max_length=50)),
                ('text_end', models.TextField()),
                ('but_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HeaderTop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('icon', models.CharField(max_length=5)),
                ('adress', models.CharField(max_length=250)),
            ],
        ),
    ]
