# Generated by Django 4.0.5 on 2022-06-27 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0004_add_vehicle'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='washing_and_cleaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('Summary', models.TextField(null=True)),
                ('price', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('discription', models.TextField(null=True)),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='garage.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='tyres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('Summary', models.TextField(null=True)),
                ('price', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('discription', models.TextField(null=True)),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='garage.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='running_repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('Summary', models.TextField(null=True)),
                ('price', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('discription', models.TextField(null=True)),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='garage.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='cable_replacement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('Summary', models.TextField(null=True)),
                ('price', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('discription', models.TextField(null=True)),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='garage.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='brakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('Summary', models.TextField(null=True)),
                ('price', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('discription', models.TextField(null=True)),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='garage.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('Summary', models.TextField(null=True)),
                ('price', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('discription', models.TextField(null=True)),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='garage.vehicle')),
            ],
        ),
    ]
