# Generated by Django 3.1.3 on 2020-11-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecepiesSite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='date',
            field=models.DateField(auto_now_add=True, default='2012-09-04'),
            preserve_default=False,
        ),
    ]
