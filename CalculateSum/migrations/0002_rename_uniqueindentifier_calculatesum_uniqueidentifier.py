# Generated by Django 3.2.5 on 2021-07-24 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CalculateSum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calculatesum',
            old_name='uniqueIndentifier',
            new_name='uniqueIdentifier',
        ),
    ]