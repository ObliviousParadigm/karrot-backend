# Generated by Django 2.0.1 on 2018-02-22 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0008_auto_20180126_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationparticipant',
            name='email_notifications',
            field=models.BooleanField(default=True),
        ),
    ]