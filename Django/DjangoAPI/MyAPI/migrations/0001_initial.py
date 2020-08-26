# Generated by Django 3.0.6 on 2020-05-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=200)),
                ('Lastname', models.CharField(max_length=200)),
                ('Prgnency', models.IntegerField(default=0)),
                ('Glucose', models.IntegerField(default=0)),
                ('Bloodpressure', models.IntegerField(default=0)),
                ('Skinthikness', models.IntegerField(default=0)),
                ('Insulin', models.IntegerField(default=0)),
                ('BMI', models.IntegerField(default=0)),
                ('DiabetesPedigreeFunction', models.IntegerField(default=0)),
                ('Age', models.IntegerField(default=0)),
            ],
        ),
    ]
