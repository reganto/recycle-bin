# Generated by Django 3.2.15 on 2022-09-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Title of the article', max_length=1025, unique=True, verbose_name='Title')),
                ('body', models.TextField(help_text='Body of the article', verbose_name='Body')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
