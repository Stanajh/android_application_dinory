# Generated by Django 3.1.7 on 2021-03-25 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0016_auto_20210324_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='img',
            field=models.ImageField(upload_to='%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='note',
            name='img',
            field=models.ImageField(upload_to='%Y/%m/%d'),
        ),
    ]
