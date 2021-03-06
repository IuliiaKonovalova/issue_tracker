# Generated by Django 3.2 on 2022-02-16 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20220214_0821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='project',
            name='slug',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_body',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
