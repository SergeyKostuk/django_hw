# Generated by Django 2.2.1 on 2019-05-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw21', '0002_auto_20190529_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='track',
        ),
        migrations.AddField(
            model_name='album',
            name='track',
            field=models.ManyToManyField(related_name='persons', to='hw21.Track'),
        ),
    ]