# Generated by Django 3.0.5 on 2020-08-05 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_questions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=300)),
                ('question_type', models.CharField(max_length=300)),
                ('query', models.CharField(max_length=800)),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
