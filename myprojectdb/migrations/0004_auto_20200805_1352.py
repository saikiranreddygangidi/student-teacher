# Generated by Django 3.0.5 on 2020-08-05 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectdb', '0003_auto_20200805_1339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_questions',
            old_name='image',
            new_name='error_image',
        ),
    ]
