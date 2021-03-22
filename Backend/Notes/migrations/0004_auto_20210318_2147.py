# Generated by Django 3.1.7 on 2021-03-18 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20210318_1854'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Notes', '0003_auto_20210318_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentence',
            name='diary',
        ),
        migrations.CreateModel(
            name='DiaryToSentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.child')),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.diary')),
                ('sentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.sentence')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]