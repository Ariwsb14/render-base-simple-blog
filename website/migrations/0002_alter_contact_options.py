# Generated by Django 4.2.16 on 2024-10-26 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created_date']},
        ),
    ]
