# Generated by Django 4.2 on 2023-07-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_delete_subjectname_student_user_classe'),
    ]

    operations = [
        migrations.CreateModel(
            name='subjectname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name1', models.CharField(max_length=100)),
                ('sub_name2', models.CharField(max_length=100)),
                ('sub_name3', models.CharField(max_length=100)),
                ('sub_name4', models.CharField(max_length=100)),
                ('sub_name5', models.CharField(max_length=100)),
                ('sub_name6', models.CharField(max_length=100)),
                ('sub_name7', models.CharField(max_length=100)),
                ('sub_name8', models.CharField(max_length=100)),
            ],
        ),
    ]
