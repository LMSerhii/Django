# Generated by Django 4.2 on 2023-04-06 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=355)),
                ('category', models.CharField(choices=[('a', 'Sci-Fi'), ('b', 'Romance'), ('c', 'Action'), ('d', 'Horror'), ('e', 'Thriller'), ('f', 'Comedy')], max_length=1)),
            ],
        ),
    ]