# Generated by Django 3.0.7 on 2020-08-01 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Practitioner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('available', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('accreditation', models.CharField(blank=True, max_length=100, null=True)),
                ('license', models.CharField(blank=True, max_length=100, null=True)),
                ('is_remote', models.BooleanField(default=False)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('school', models.CharField(blank=True, max_length=200, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='practitioner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
