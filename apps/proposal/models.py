from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Team(models.Model):
    proposal = models.ForeignKey('Proposal', on_delete=models.CASCADE)
    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200)
    degree = models.CharField('Education Degree', max_length=200, blank=True, null=True)
    position = models.CharField(max_length=250, blank=True, null=True)
    role = models.CharField('Role in this research', max_length=250, blank=True, null=True)


class References(models.Model):
    proposal = models.ForeignKey('Proposal', on_delete=models.CASCADE)
    doi = models.CharField('DOI', max_length=250, unique=True, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    reference = models.CharField('full reference', max_length=250, blank=True, null=True)


class Budget(models.Model):
    proposal = models.ForeignKey('Proposal', on_delete=models.CASCADE)
    item = models.CharField(max_length=250)
    justification = models.CharField(max_length=250, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)


class WorkPlan(models.Model):
    proposal = models.ForeignKey('Proposal', on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)


class Appendices(models.Model):
    proposal = models.ForeignKey('Proposal', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    attachment = models.FileField(upload_to='proposal/')


class Proposal(models.Model):
    DRAFT = 'DR'
    REQUIRING_ATTENTION = 'RA'
    UNDER_REVIEW = 'UR'
    POST_REVIEW = 'PR'
    WITHDRAWN = 'WD'
    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (REQUIRING_ATTENTION, 'Requiring attention'),
        (UNDER_REVIEW, 'Under Review'),
        (POST_REVIEW, 'Post-Review'),
        (WITHDRAWN, 'Withdrawn'),
    )
    title = models.CharField(max_length=250, unique=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    abstract = RichTextField(blank=True, null=True)
    background = RichTextField(blank=True, null=True)
    project_history = RichTextField('project history', blank=True, null=True,)
    data_collection = RichTextField('data collection & analysis', blank=True, null=True)
    goal = RichTextField('goal & strategy', blank=True, null=True)
    audiences = RichTextField(blank=True, null=True)
    impact = RichTextField('impact on community', blank=True, null=True)
    supervisor = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='Supervisor', blank=True)
    pi = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='PI', blank=True, null=True)
    co_pi = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='Co_PI', blank=True, null=True)
    referee = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='Referee', blank=True, null=True)
    secretary = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='Secretary', blank=True, null=True)
    created_at = models.DateTimeField('created date', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField('updated date', auto_now=True, blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DRAFT)

    def __str__(self):
        return self.title


