# Generated by Django 4.1.7 on 2023-04-03 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marni', '0002_article_reporter_delete_post_article_reporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]
