# Generated by Django 4.1.4 on 2023-01-06 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_blog_delete_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='status',
        ),
    ]
