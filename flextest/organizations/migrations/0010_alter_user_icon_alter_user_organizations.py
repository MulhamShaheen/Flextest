# Generated by Django 4.1.7 on 2023-02-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0009_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(blank=True, upload_to='uploads/users/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='organizations',
            field=models.ManyToManyField(blank=True, to='organizations.organization'),
        ),
    ]
