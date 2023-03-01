# Generated by Django 4.1.6 on 2023-02-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_contact_description_contact_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
                ('phone', models.IntegerField()),
                ('proj', models.CharField(choices=[('drone', 'Drone_detection'), ('pothole', 'Pothole_counter'), ('facemask', 'Facemask_detection'), ('tooth', 'tooth_detection')], max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
