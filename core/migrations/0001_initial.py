# Generated by Django 3.2.7 on 2021-09-06 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_date', models.DateTimeField()),
                ('approved', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('width', models.IntegerField()),
                ('length', models.IntegerField()),
                ('number_of_rooms', models.PositiveIntegerField()),
                ('number_of_bathrooms', models.PositiveIntegerField()),
                ('funiture_ready', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=50)),
                ('sale_type', models.CharField(choices=[('Rent', 'Rent'), ('Sale', 'Sale')], max_length=5)),
                ('coverphoto', models.ImageField(upload_to='media/<django.db.models.fields.CharField>/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
