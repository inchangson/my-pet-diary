# Generated by Django 2.2.5 on 2022-01-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0003_auto_20220123_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletinfeed',
            name='txt_path',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
