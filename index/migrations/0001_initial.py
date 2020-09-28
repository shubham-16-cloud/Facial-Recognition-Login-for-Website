# Generated by Django 3.1 on 2020-08-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('subtext', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='img/')),
                ('dateofinsert', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_date', models.DateField()),
                ('event_title', models.CharField(max_length=1000)),
                ('event_text', models.CharField(max_length=1000)),
                ('event_img', models.ImageField(upload_to='img/event/')),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('news_date', models.DateField()),
                ('news_title', models.CharField(max_length=1000)),
                ('news_text', models.CharField(max_length=1000)),
                ('news_img', models.ImageField(upload_to='img/news/')),
            ],
        ),
    ]
