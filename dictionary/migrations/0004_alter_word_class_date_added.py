# Generated by Django 3.2.4 on 2021-06-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_auto_20210607_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word_class',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]