# Generated by Django 3.0.6 on 2020-05-26 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('debut_date', models.DateField()),
                ('member', models.TextField()),
                ('description', models.TextField()),
                ('interest', models.PositiveIntegerField(default=0)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='indiecator/')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('poster', models.ImageField(blank=True, null=True, upload_to='indiecator/')),
                ('artists', models.ManyToManyField(to='indiecator_app.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('commented_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indiecator_app.Event')),
            ],
        ),
    ]
