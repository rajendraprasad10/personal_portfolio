# Generated by Django 2.2.4 on 2019-09-03 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190903_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='portfolio_type',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
    ]
