# Generated by Django 4.0.6 on 2022-07-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_remove_home_linkedin_remove_social_email_home_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AddField(
            model_name='project',
            name='image_link',
            field=models.URLField(default='https://images.unsplash.com/photo-1658905900633-b0af9daed14e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80'),
        ),
    ]