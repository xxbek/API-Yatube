# Generated by Django 4.0.6 on 2022-08-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_group_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='title',
            field=models.CharField(default='Some title', max_length=200),
        ),
    ]