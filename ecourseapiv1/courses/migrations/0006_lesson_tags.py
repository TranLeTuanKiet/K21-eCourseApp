# Generated by Django 5.0.3 on 2024-03-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_rename_category_lesson_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(to='courses.tag'),
        ),
    ]