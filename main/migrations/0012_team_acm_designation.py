# Generated by Django 4.0.4 on 2022-04-24 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_team_gender_alter_mentor_image_alter_team_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='acm_designation',
            field=models.CharField(default='Member', max_length=50),
        ),
    ]
