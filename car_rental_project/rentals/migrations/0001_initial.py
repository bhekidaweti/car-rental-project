# Generated by Django 4.2.13 on 2024-06-11 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('vehicle_type', models.CharField(choices=[('SUV', 'SUV'), ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('Truck', 'Truck'), ('Bus', 'Bus')], max_length=30)),
                ('description', models.TextField()),
                ('daily_rates', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='vehicle_images/')),
            ],
        ),
    ]
