# Generated by Django 2.0.6 on 2018-06-18 14:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0028_add_group_names_view_20180310_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='last_active_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]