# Generated by Django 3.2 on 2021-04-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gov_thai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('FirstPrize', models.CharField(max_length=20)),
                ('ThreeFront', models.CharField(max_length=20)),
                ('ThreeFrontTwo', models.CharField(max_length=20)),
                ('ThreeUnder', models.CharField(max_length=20)),
                ('ThreeUnderTwo', models.CharField(max_length=20)),
                ('TwoUnder', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=30)),
            ],
        ),
    ]
