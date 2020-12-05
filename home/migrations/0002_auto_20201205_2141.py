# Generated by Django 3.1.3 on 2020-12-05 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registeration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll_no', models.IntegerField()),
                ('img', models.ImageField(upload_to='FaceImages', verbose_name='Profile Picture')),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=4)),
            ],
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]