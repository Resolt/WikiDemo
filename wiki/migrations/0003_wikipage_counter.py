# Generated by Django 4.0.1 on 2022-01-29 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_alter_wikipage_text_alter_wikipage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikipage',
            name='counter',
            field=models.BigIntegerField(default=0),
        ),
    ]
