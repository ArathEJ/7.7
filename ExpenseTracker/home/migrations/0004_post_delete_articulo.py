# Generated by Django 4.1 on 2022-11-14 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_addmoney_info_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('intro', models.TextField()),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.DeleteModel(
            name='Articulo',
        ),
    ]
