# Generated by Django 4.2.6 on 2023-11-02 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(default=0)),
                ('productname', models.CharField(max_length=50)),
                ('productprice', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
