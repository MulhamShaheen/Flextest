# Generated by Django 4.1.7 on 2023-02-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0002_remove_user_firstname_remove_user_surname_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="user",
            name="staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="icon",
            field=models.ImageField(blank=True, upload_to="uploads/users/"),
        ),
        migrations.AlterField(
            model_name="user",
            name="organizations",
            field=models.ManyToManyField(blank=True, to="organizations.organization"),
        ),
    ]
