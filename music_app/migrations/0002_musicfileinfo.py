# Generated by Django 2.2.4 on 2019-08-11 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('music', models.FileField(upload_to='musics/')),
                ('musicid', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]