# Generated by Django 3.0 on 2019-12-16 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicleowner', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presigned_url', models.CharField(max_length=255, verbose_name='Presigned Url')),
                ('size', models.IntegerField(verbose_name='Size')),
                ('doc_type', models.CharField(max_length=15, verbose_name='Doc Type')),
            ],
        ),
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('zip_code', models.CharField(max_length=128, verbose_name='Zipcode')),
                ('city', models.CharField(db_index=True, max_length=128, verbose_name='City')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='advertiser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('advertiser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='advertiser.Advertiser')),
                ('document_file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='advertiser.Document')),
                ('vehicle_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vehicleowner.VehicleOwner')),
            ],
        ),
    ]
