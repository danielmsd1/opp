# Generated by Django 4.0.6 on 2022-07-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_art'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
