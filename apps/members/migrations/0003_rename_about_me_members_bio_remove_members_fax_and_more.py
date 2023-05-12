# Generated by Django 4.0.5 on 2023-05-08 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0002_alter_members_options_members_other'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='about_me',
            new_name='bio',
        ),
        migrations.RemoveField(
            model_name='members',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='members',
            name='member_number',
        ),
        migrations.AddField(
            model_name='members',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='members',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='members',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='members',
            name='profile_pic',
            field=models.ImageField(blank=True, default='member/avatar.png', null=True, upload_to='member/', verbose_name='Profile Picture'),
        ),
    ]
