# Generated by Django 3.0.4 on 2020-08-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default=0)),
                ('update_desc', models.CharField(max_length=500)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
