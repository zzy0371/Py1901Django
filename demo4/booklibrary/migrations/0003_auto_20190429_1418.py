# Generated by Django 2.2 on 2019-04-29 06:18

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('booklibrary', '0002_hotpic'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('message', tinymce.models.HTMLField()),
            ],
        ),
        migrations.AlterField(
            model_name='hotpic',
            name='pic',
            field=models.ImageField(upload_to='hotpic/'),
        ),
    ]
