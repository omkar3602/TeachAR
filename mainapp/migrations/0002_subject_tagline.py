# Generated by Django 4.1.2 on 2022-10-16 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='tagline',
            field=models.CharField(default='This is subject tagline', max_length=50),
            preserve_default=False,
        ),
    ]
