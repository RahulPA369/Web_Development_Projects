# Generated by Django 4.0.4 on 2022-05-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imagename', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='img/')),
            ],
        ),
    ]
