# Generated by Django 4.1.4 on 2023-01-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0008_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='excerpt',
            field=models.TextField(default='The ministry of the creation of man'),
            preserve_default=False,
        ),
    ]