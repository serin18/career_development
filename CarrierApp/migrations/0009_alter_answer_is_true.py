# Generated by Django 4.1.5 on 2024-03-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarrierApp', '0008_alter_answer_is_true'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='is_true',
            field=models.BooleanField(choices=[(True, 'True'), (False, 'False')], default=False),
        ),
    ]