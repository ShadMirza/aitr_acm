# Generated by Django 4.0.4 on 2022-04-24 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_team_acm_designation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='acm_designation',
            new_name='acmw_designation',
        ),
    ]
