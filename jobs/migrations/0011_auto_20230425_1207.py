# Generated by Django 3.0.5 on 2023-04-25 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_alter_applicant_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='user',
            new_name='email',
        ),
    ]
