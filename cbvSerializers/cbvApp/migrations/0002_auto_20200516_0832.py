# Generated by Django 3.0.2 on 2020-05-16 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbvApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]