# Generated by Django 4.2.2 on 2023-07-04 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('orden', models.CharField(max_length=30)),
                ('habitat', models.CharField(max_length=30)),
                ('tomaño', models.IntegerField()),
            ],
        ),
    ]
