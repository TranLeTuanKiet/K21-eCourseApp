# Generated by Django 5.0.3 on 2024-03-19 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_tag_user_avatar_alter_course_image_alter_course_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='category',
            new_name='course',
        ),
    ]
