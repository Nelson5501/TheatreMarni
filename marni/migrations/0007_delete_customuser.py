# Generated by Django 4.2.2 on 2023-06-13 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marni', '0006_customuser_delete_choice_delete_question'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]