# Generated by Django 3.2.9 on 2022-03-11 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0007_alter_colleges_minimumgpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colleges',
            name='Deadlines',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='colleges',
            name='Name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='colleges',
            name='ScholarshipName',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
