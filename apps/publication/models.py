from django.db import models
from apps.members.models import Members


# Under review Research paper model
class DraftArticles(models.Model):
    title = models.TextField()
    main_authors = models.TextField()
    other_authors = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    doi = models.CharField("DOI", max_length=100, unique=True)
    affiliation = models.TextField()
    journal = models.TextField()
    abstract = models.TextField()
    keywords = models.TextField()
    is_rural360 = models.BooleanField("Rural360")
    is_6for6 = models.BooleanField("6for6")
    is_surgecon = models.BooleanField("SurgeCon")
    # three statues
    under_review = '0'
    accept = '1'
    reject = '2'
    STATUES = [
        (under_review, 'under review'),
        (accept, 'accept'),
        (reject, 'reject'),
    ]
    statues = models.CharField(
        max_length=2,
        choices=STATUES,
        default=under_review
    )

    def __str__(self):
        return self.title

    author_list = models.ManyToManyField(Members)

    class Meta:
        db_table = "draft_articles"  # table name in the database
        verbose_name = "Under Review Articles"  # name in the admin
        verbose_name_plural = verbose_name


# Published Research paper model
class PublishedArticles(models.Model):
    title = models.TextField()
    main_authors = models.TextField()
    other_authors = models.TextField(blank=True, null=True)
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

    author_list = models.ManyToManyField(Members)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "published_articles"  # table name in the database
        verbose_name = "Published Articles"  # name in the admin
        verbose_name_plural = verbose_name


# Under review Presentation
class DraftPresentations(models.Model):
    title = models.TextField()
    main_authors = models.TextField()
    other_authors = models.TextField("collaborative authors", blank=True, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
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
    abstract = models.TextField()
    external_link = models.URLField(blank=True, null=True)
    archive = models.FileField(upload_to='publication/presentations/archive', blank=True, null=True)
    picture = models.ImageField(upload_to='publication/presentations/picture', blank=True, null=True)
    is_rural360 = models.BooleanField("Rural360")
    is_6for6 = models.BooleanField("6for6")
    is_surgecon = models.BooleanField("SurgeCon")
    # three statues
    under_review = '0'
    accept = '1'
    reject = '2'
    STATUES = [
        (under_review, 'under review'),
        (accept, 'accept'),
        (reject, 'reject'),
    ]
    statues = models.CharField(
        max_length=2,
        choices=STATUES,
        default=under_review
    )

    author_list = models.ManyToManyField(Members)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "draft_presentations"  # table name in the database
        verbose_name = "Under Review Conference Presentations"  # name in the admin
        verbose_name_plural = verbose_name


# Published presentation model
class PublishedPresentations(models.Model):
    title = models.TextField()
    main_authors = models.TextField()
    other_authors = models.TextField("collaborative authors", blank=True, null=True)
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

    author_list = models.ManyToManyField(Members)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "published_Presentations"  # table name in the database
        verbose_name = "Published Conference Presentations"  # name in the admin
        verbose_name_plural = verbose_name


# UnderReview Books model
class DraftBooks(models.Model):
    isbn = models.CharField(max_length=30, unique=True)
    title = models.TextField()
    main_authors = models.TextField()
    other_authors = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    introduction = models.TextField()
    external_link = models.URLField(blank=True, null=True)
    archive = models.FileField(upload_to='publication/books/archive', blank=True, null=True)
    picture = models.FileField("Book Cover", upload_to='publication/books/picture')
    categories = models.CharField(max_length=250)
    is_rural360 = models.BooleanField("Rural360")
    is_6for6 = models.BooleanField("6for6")
    is_surgecon = models.BooleanField("SurgeCon")
    # three statues
    under_review = '0'
    accept = '1'
    reject = '2'
    STATUES = [
        (under_review, 'under review'),
        (accept, 'accept'),
        (reject, 'reject'),
    ]
    statues = models.CharField(
        max_length=2,
        choices=STATUES,
        default=under_review
    )

    author_list = models.ManyToManyField(Members)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "draft_books"  # table name in the database
        verbose_name = "Under Review Books"  # name in the admin
        verbose_name_plural = verbose_name


# Published Books model
class PublishedBooks(models.Model):

    isbn = models.CharField(max_length=30, unique=True)
    title = models.TextField()
    main_authors = models.TextField()
    other_authors = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    introduction = models.TextField()
    external_link = models.URLField(blank=True, null=True)
    archive = models.FileField(upload_to='publication/books/archive', blank=True, null=True)
    picture = models.FileField("Book Cover", upload_to='publication/books/picture')
    categories = models.CharField(max_length=250)
    is_rural360 = models.BooleanField("Rural360")
    is_6for6 = models.BooleanField("6for6")
    is_surgecon = models.BooleanField("SurgeCon")
    is_published = models.BooleanField("Publish")

    author_list = models.ManyToManyField(Members)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "published_Books"  # table name in the database
        verbose_name = "Published Books"  # name in the admin
        verbose_name_plural = verbose_name


# Under review online model
class DraftOnline(models.Model):
    title = models.TextField()
    main_authors = models.TextField()
    other_authors = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    abstract = models.TextField()
    external_link = models.URLField(blank=True, null=True)
    is_rural360 = models.BooleanField("Rural360")
    is_6for6 = models.BooleanField("6for6")
    is_surgecon = models.BooleanField("SurgeCon")
    # three statues
    under_review = '0'
    accept = '1'
    reject = '2'
    STATUES = [
        (under_review, 'under review'),
        (accept, 'accept'),
        (reject, 'reject'),
    ]
    statues = models.CharField(
        max_length=2,
        choices=STATUES,
        default=under_review
    )

    author_list = models.ManyToManyField(Members)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "draft_online"  # table name in the database
        verbose_name = "Under Review Online"  # name in the admin
        verbose_name_plural = verbose_name


# Published online model
class PublishedOnline(models.Model):
    title = models.TextField()
    main_authors = models.TextField()
    other_authors = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    abstract = models.TextField()
    external_link = models.URLField(blank=True, null=True)
    is_rural360 = models.BooleanField("Rural360")
    is_6for6 = models.BooleanField("6for6")
    is_surgecon = models.BooleanField("SurgeCon")
    is_published = models.BooleanField("Publish")

    author_list = models.ManyToManyField(Members)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "published_online"  # table name in the database
        verbose_name = "Published Online"  # name in the admin
        verbose_name_plural = verbose_name
