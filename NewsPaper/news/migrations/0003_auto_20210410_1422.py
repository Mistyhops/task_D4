# Generated by Django 3.1.7 on 2021-04-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], max_length=2),
        ),
    ]
