# Generated by Django 2.2.5 on 2020-06-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_metrobus', '0006_auto_20200611_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='question1',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='question3',
        ),
        migrations.AlterField(
            model_name='bug',
            name='type',
            field=models.CharField(choices=[('technical', 'Technisches Problem'), ('usage', 'Schwierigkeit bei der Nutzung der App'), ('content', 'Inkorrekter oder unverständlicher Inhalt'), ('other', 'Anderes')], default=None, max_length=20, verbose_name='Problem'),
        ),
    ]
