# Generated by Django 5.1.7 on 2025-03-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oiproblems', '0002_announcement_group_user_match_problem_match_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_type',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
