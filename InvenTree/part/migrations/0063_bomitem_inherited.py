# Generated by Django 3.0.7 on 2021-02-17 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0062_merge_20210105_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='bomitem',
            name='inherited',
            field=models.BooleanField(default=False, help_text='This BOM item is inherited by BOMs for variant parts', verbose_name='Inherited'),
        ),
    ]