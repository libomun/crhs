# Generated by Django 4.0.5 on 2023-05-22 23:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_comment_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='BottomInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='home/', verbose_name='image')),
                ('bottom_info', models.CharField(blank=True, choices=[('info1', 'Bottom Info 1'), ('info2', 'Bottom Info 2'), ('info3', 'Bottom Info 3')], max_length=20, null=True, verbose_name='bottom information')),
            ],
            options={
                'verbose_name': 'bottom info',
                'verbose_name_plural': 'bottom info',
                'db_table': 'bottom info',
            },
        ),
        migrations.CreateModel(
            name='HeadlineNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('affiliation', models.CharField(blank=True, max_length=100, null=True, verbose_name='affiliation')),
                ('external_link', models.URLField(blank=True, null=True, verbose_name='external link')),
                ('published_date', models.DateTimeField(verbose_name='date published')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('news_content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('cover_img', models.ImageField(upload_to='home/', verbose_name='cover image')),
                ('is_publish', models.BooleanField(default=True, verbose_name='publish')),
                ('headline', models.CharField(blank=True, choices=[('headline1', 'Headline 1'), ('headline2', 'Headline 2'), ('headline3', 'Headline 3')], max_length=20, null=True, verbose_name='headline')),
            ],
            options={
                'verbose_name': 'headline news',
                'verbose_name_plural': 'headline news',
                'db_table': 'headline news',
            },
        ),
        migrations.RemoveField(
            model_name='news',
            name='is_headline',
        ),
    ]