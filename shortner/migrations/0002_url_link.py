# Generated by Django 3.2.5 on 2021-07-29 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='link',
            field=models.CharField(default=1, max_length=10000),
            preserve_default=False,
        ),
    ]
