# Generated by Django 3.1.4 on 2020-12-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20201230_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuote',
            name='product_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]