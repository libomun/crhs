from django.db import models
from ckeditor.fields import RichTextField


# Rural360 Draft News model
class Rural360DraftNews(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    username = models.CharField("username (The same as login username)", max_length=100)  # filter news that created by himself
    created_date = models.DateTimeField("date created", auto_now_add=True)  # first created time
    updated_date = models.DateTimeField("date updated", auto_now=True)  # updated time for news
    news_text = RichTextField(blank=True, null=True)
    news_img = models.ImageField("news image", upload_to='rural360/news/')
    # three statues
    in_processing = '0'
    approved = '1'
    unapproved = '2'
    STATUES = [
        (in_processing, 'in processing'),
        (approved, 'approved'),
        (unapproved, 'unapproved'),
    ]
    statues = models.CharField(
        max_length=2,
        choices=STATUES,
        default=in_processing
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "rural360_draft_news"  # table name in the database
        verbose_name = "Rural360 draft news"  # name in the admin site
        verbose_name_plural = verbose_name


# Rural360 Published news model
class Rural360PublishedNews(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    news_type = models.CharField("news type", max_length=20, default='rural360')
    published_date = models.DateTimeField("date published", auto_now_add=True)  # first published time
    updated_date = models.DateTimeField("date updated", auto_now=True)  # updated time for news, not show in the webpage
    news_text = RichTextField(blank=True, null=True)
    news_img = models.ImageField("news image", upload_to='news/rural360')
    is_publish = models.BooleanField("publish", default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "rural360_published_news"  # table name in the database
        verbose_name = "Rural360 published news"  # name in the admin site
        verbose_name_plural = verbose_name


# 6for6 Draft News model
class SixforsixDraftNews(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    username = models.CharField("username (The same as login username)", max_length=100)  # filter news that created by himself
    created_date = models.DateTimeField("date created", auto_now_add=True)  # first created time
    updated_date = models.DateTimeField("date updated", auto_now=True)  # updated time for news
    news_text = RichTextField(blank=True, null=True)
    news_img = models.ImageField("news image", upload_to='news/sixforsix')
    # three statues
    in_processing = '0'
    approved = '1'
    unapproved = '2'
    STATUES = [
        (in_processing, 'in processing'),
        (approved, 'approved'),
        (unapproved, 'unapproved'),
    ]
    statues = models.CharField(
        max_length=2,
        choices=STATUES,
        default=in_processing
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "sixforsix_draft_news"  # table name in database
        verbose_name = "6for6 draft news"  # name in the admin site
        verbose_name_plural = verbose_name


# 6for6 Published news model
class SixforsixPublishedNews(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    news_type = models.CharField("news type", max_length=20, default='sixforsix')
    published_date = models.DateTimeField("date published", auto_now_add=True)  # first published time
    updated_date = models.DateTimeField("date updated", auto_now=True)  # updated time for 6for6, not show in the webpage
    news_text = RichTextField(blank=True, null=True)
    news_img = models.ImageField("news image", upload_to='news/sixforsix')
    is_publish = models.BooleanField("publish", default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "sixforsix_published_news"  # table name in the database
        verbose_name = "6for6 published news"  # name in the admin site
        verbose_name_plural = verbose_name


# SurgeCon draft news model
class SurgeConDraftNews(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    username = models.CharField("username (The same as login username)", max_length=100)  # filter news that created by himself
    created_date = models.DateTimeField("date created", auto_now_add=True)  # first created time
    updated_date = models.DateTimeField("date updated", auto_now=True)  # updated time for news
    news_text = RichTextField(blank=True, null=True)
    news_img = models.ImageField("news image", upload_to='news/surgecon')
    # three statues
    in_processing = '0'
    approved = '1'
    unapproved = '2'
    STATUES = [
        (in_processing, 'in processing'),
        (approved, 'approved'),  # approved and published
        (unapproved, 'unapproved'),
    ]
    statues = models.CharField(
        max_length=2,
        choices=STATUES,
        default=in_processing
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "surgecon_draft_news"  # table name in the database
        verbose_name = "SurgeCon draft news"  # name in the admin site
        verbose_name_plural = verbose_name


# SurgeCon published news model
class SurgeConPublishedNews(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    news_type = models.CharField("news type", max_length=20, default='surgecon')
    published_date = models.DateTimeField("date published", auto_now_add=True)  # first published time
    updated_date = models.DateTimeField("date updated", auto_now=True)  # updated time for news, not show in the webpage
    news_text = RichTextField(blank=True, null=True)
    news_img = models.ImageField("news image", upload_to='news/surgecon')
    is_publish = models.BooleanField("publish", default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "surgecon_published_news"  # table name in the database
        verbose_name = "SurgeCon published news"  # name in the admin site
        verbose_name_plural = verbose_name






