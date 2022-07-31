# Generated by Django 4.0.5 on 2022-07-05 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_battery_brakes_cable_replacement_regular_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('garage', '0004_add_vehicle'),
        ('booking', '0013_alter_cart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
                ('package', models.CharField(max_length=255)),
                ('date', models.DateField(null=True)),
                ('states', models.BooleanField(null=True)),
                ('price_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.price_model')),
                ('user', models.ForeignKey(default='N/A', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='garage.vehicle')),
            ],
        ),
    ]
