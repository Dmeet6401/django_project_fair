# Generated by Django 4.1.6 on 2023-02-15 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_drone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122, verbose_name='drone_image')),
                ('drone_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]