from ckeditor.fields import RichTextField
from django.conf import settings
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models


# Faculty and staff model
class Members(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    affiliation = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField("Profile Picture", default="member/avatar.png", upload_to='member/', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField( max_length=20, blank=True, null=True)
    office_address = models.CharField(max_length=200, blank=True, null=True)
    bio = RichTextField(blank=True, null=True)
    external_link = models.URLField(max_length=200, blank=True, null=True)

    FACULTY = 'faculty'
    STAFF = 'staff'
    GRADUATE = 'graduate'
    UNDERGRADUATE = 'undergraduate'
    RA = 'ra'
    POSTDOCS = 'postdocs'
    ALUMNI = 'alumni'
    OTHER = 'other'

    ROLE_CHOICES = (
        (FACULTY, 'Faculty'),
        (STAFF, 'Staff'),
        (GRADUATE, 'Graduate Students'),
        (UNDERGRADUATE, 'Undergraduate Students'),
        (RA, 'Research Assistant'),
        (POSTDOCS, 'Postdoctoral Researcher'),
        (ALUMNI, 'Alumni'),
        (OTHER, 'Other'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, blank=True, null=True)
    is_active = models.BooleanField("Active", default='True')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Members"  # name in the admin site
        verbose_name_plural = verbose_name

