# Generated by Django 4.0.2 on 2022-04-07 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papp', '0002_alter_question_pub_date_alter_question_question_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='asking',
        ),
    ]
