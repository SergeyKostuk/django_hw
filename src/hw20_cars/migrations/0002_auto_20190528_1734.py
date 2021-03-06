# Generated by Django 2.2.1 on 2019-05-28 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hw20_cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default=None, max_length=50, null=True)),
                ('address', models.CharField(default=None, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='contact_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person', to='hw20_cars.ContactInfo'),
        ),
    ]
