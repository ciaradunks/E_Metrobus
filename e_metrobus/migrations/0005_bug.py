# Generated by Django 2.2.5 on 2020-06-11 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_metrobus', '0004_auto_20200403_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('error', 'Fehler'), ('design', 'Design'), ('other', 'Sonstiges')], max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
