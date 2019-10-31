# Generated by Django 2.2.1 on 2019-05-29 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hw21', '0006_auto_20190529_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alb', to='hw21.MusicBand'),
        ),
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='track', to='hw21.Album'),
        ),
    ]