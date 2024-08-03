# Generated by Django 4.2.7 on 2023-12-15 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'Customer'), (2, 'Event Provider')], default=1),
        ),
    ]
