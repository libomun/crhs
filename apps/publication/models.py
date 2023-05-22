from django.conf import settings
from django.db import models
from apps.members.models import Members


# Published Research paper model
class Articles(models.Model):
    title = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    main_authors = models.TextField()
    other_authors = models.TextField(blank=True, null=True)
    author_list = models.ManyToManyField(Members)
    date = models.DateField(auto_now=False, auto_now_add=False)
    doi = models.CharField("DOI", max_length=100, unique=True)
    affiliation = models.TextField()
    journal = models.TextField()
    abstract = models.TextField()
    keywords = models.CharField(max_length=250)
    is_rural360 = models.BooleanField("Rural360")
    is_6for6 = models.BooleanField("6for6")
    is_surgecon = models.BooleanField("SurgeCon")
    is_published = models.BooleanField("Publish")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "articles"  # table name in the database
        verbose_name = "Articles"  # name in the admin
        verbose_name_plural = verbose_name


# Published presentation model
class Presentations(models.Model):
    title = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    main_authors = models.TextField()
    other_authors = models.TextField("collaborative authors", blank=True, null=True)
    author_list = models.ManyToManyField(Members)
    date = models.DateField(auto_now=False, auto_now_add=False)
    abstract = models.TextField()
    # three statues
    oral = '0'
    poster = '1'
    workshop = '2'
    STATUES = [
        (oral, 'oral'),
        (poster, 'poster'),
        (workshop, 'workshop'),
    ]
    types = models.CharField(
        max_length=2,
        choices=STATUES,
        null=True,
    )

    external_link = models.URLField(blank=True, null=True)
    archive = models.FileField(upload_to='publication/presentations/archive', blank=True, null=True)
    picture = models.ImageField(upload_to='publication/presentations/picture', blank=True, null=True)
    is_rural360 = models.BooleanField("Rural360")
    is_6for6 = models.BooleanField("6for6")
    is_surgecon = models.BooleanField("SurgeCon")
    is_published = models.BooleanField("Publish")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "presentations"  # table name in the database
        verbose_name = "Conference Presentations"  # name in the admin
        verbose_name_plural = verbose_name


# Published Books model
class Books(models.Model):

    isbn = models.CharField(max_length=30, unique=True)
    title = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    main_authors = models.TextField()
    other_authors = models.TextField(blank=True, null=True)
    author_list = models.ManyToManyField(Members)
    date = models.DateField(auto_now=False, auto_now_add=False)
    introduction = models.TextField()
    external_link = models.URLField(blank=True, null=True)
    archive = models.FileField(upload_to='publication/books/archive', blank=True, null=True)
    picture = models.ImageField("Book Cover", upload_to='publication/books/picture')
    categories = models.CharField(max_length=250)
    is_rural360 = models.BooleanField("Rural360")
    is_6for6 = models.BooleanField("6for6")
    is_surgecon = models.BooleanField("SurgeCon")
    is_published = models.BooleanField("Publish")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "books"  # table name in the database
        verbose_name = "Books"  # name in the admin
        verbose_name_plural = verbose_name


# Published online model
class Online(models.Model):
    title = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    main_authors = models.TextField()
    other_authors = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    author_list = models.ManyToManyField(Members)
    abstract = models.TextField()
    external_link = models.URLField(blank=True, null=True)
    is_rural360 = models.BooleanField("Rural360")
    is_6for6 = models.BooleanField("6for6")
    is_surgecon = models.BooleanField("SurgeCon")
    is_published = models.BooleanField("Publish")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "online"  # table name in the database
        verbose_name = "Online"  # name in the admin
        verbose_name_plural = verbose_name
