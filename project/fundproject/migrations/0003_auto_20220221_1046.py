# Generated by Django 3.2.10 on 2022-02-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundproject', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='projectreports',
            name='message',
            field=models.CharField(max_length=100),
        ),
    ]
