# Generated by Django 2.2.28 on 2023-04-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewMo3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BigIntegerField()),
            ],
        ),
    ]