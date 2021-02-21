# Generated by Django 3.1.6 on 2021-02-21 22:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('creation_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('admin', models.BooleanField(default=False)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usergui.client')),
            ],
        ),
    ]
