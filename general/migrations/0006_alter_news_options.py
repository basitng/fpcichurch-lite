# Generated by Django 4.1.4 on 2023-01-06 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_news_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-published'], 'verbose_name': 'Latest News', 'verbose_name_plural': 'News'},
        ),
    ]
