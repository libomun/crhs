from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField


# News model
class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True, null=True)
    affiliation = models.CharField("affiliation", max_length=100, blank=True, null=True)
    external_link = models.URLField('external link', blank=True, null=True)
    published_date = models.DateTimeField("date published", auto_now=False, auto_now_add=False)  # published time
    updated_date = models.DateTimeField("date updated", auto_now=True)  # updated time for news, not show in the webpage
    news_content = RichTextField(blank=True, null=True)
    cover_img = models.ImageField("cover image", upload_to='news/')
    is_publish = models.BooleanField("publish", default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "news"  # table name in the database
        verbose_name = "news"  # name in the admin site
        verbose_name_plural = verbose_name


# Comment model
class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    body = models.TextField('comment')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_date']


# Head News model
class HeadlineNews(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True, null=True)
    affiliation = models.CharField("affiliation", max_length=100, blank=True, null=True)
    external_link = models.URLField('external link', blank=True, null=True)
    published_date = models.DateTimeField("date published", auto_now=False, auto_now_add=False)  # published time
    updated_date = models.DateTimeField("date updated", auto_now=True)  # updated time for news, not show in the webpage
    news_content = RichTextField(blank=True, null=True)
    cover_img = models.ImageField("cover image", upload_to='home/')
    HEADLINE_CHOICES = (
        ('headline1', 'Headline 1'),
        ('headline2', 'Headline 2'),
        ('headline3', 'Headline 3'),
    )
    headline = models.CharField("headline", max_length=20, choices=HEADLINE_CHOICES, null=True, blank=True)
    is_publish = models.BooleanField("publish", default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "headline news"  # table name in the database
        verbose_name = "headline news"  # name in the admin site
        verbose_name_plural = verbose_name


# Head News model
class BottomInfo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    img = models.ImageField("image", upload_to='home/')
    INFO_CHOICES = (
        ('info1', 'Bottom Info 1'),
        ('info2', 'Bottom Info 2'),
        ('info3', 'Bottom Info 3'),
    )
    bottom_info = models.CharField("bottom information", max_length=20, choices=INFO_CHOICES, null=True, blank=True)
    is_publish = models.BooleanField("publish", default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "bottom info"  # table name in the database
        verbose_name = "bottom info"  # name in the admin site
        verbose_name_plural = verbose_name

