# Generated by Django 4.0.5 on 2023-05-08 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_rename_about_me_members_bio_remove_members_fax_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='is_alumni',
        ),
        migrations.RemoveField(
            model_name='members',
            name='is_faculty',
        ),
        migrations.RemoveField(
            model_name='members',
            name='is_graduate',
        ),
        migrations.RemoveField(
            model_name='members',
            name='is_postdocs',
        ),
        migrations.RemoveField(
            model_name='members',
            name='is_ra',
        ),
        migrations.RemoveField(
            model_name='members',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='members',
            name='is_undergrad',
        ),
        migrations.RemoveField(
            model_name='members',
            name='other',
        ),
        migrations.AddField(
            model_name='members',
            name='role',
            field=models.CharField(blank=True, choices=[('faculty', 'Faculty'), ('staff', 'Staff'), ('graduate', 'Graduate Students'), ('undergraduate', 'Undergraduate Students'), ('ra', 'Research Assistant'), ('postdocs', 'Postdoctoral Researcher'), ('alumni', 'Alumni'), ('other', 'Other')], max_length=50, null=True),
        ),
    ]