# Generated by Django 3.2.16 on 2022-10-21 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('I', 'Import Cars'), ('BF', 'Baby Food'), ('F', 'Furniture')], max_length=2),
        ),
    ]
