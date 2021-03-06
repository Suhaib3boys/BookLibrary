# Generated by Django 4.0.3 on 2022-03-30 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_name', models.CharField(max_length=70)),
                ('Publish_year', models.IntegerField()),
                ('Book_description', models.TextField(max_length=350)),
                ('Writer', models.CharField(max_length=70)),
                ('Image', models.ImageField(upload_to='IMG')),
            ],
        ),
    ]
