from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models


# Faculty and staff model
class Members(models.Model):
    member_number = models.CharField(max_length=4,  unique=True, validators=[RegexValidator('^[0-9]{4}', message='Personnel value must be number'), MinLengthValidator(4, message='Ensure this value has at least 4 numbers')])
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100, blank=True, null=True)
    affiliation = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField("Profile Picture", upload_to='member/', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField( max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    office_address = models.CharField(max_length=200, blank=True, null=True)
    about_me = RichTextField(blank=True, null=True)
    external_link = models.URLField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField("Active", default='True')
    is_faculty = models.BooleanField("Faculty")
    is_staff = models.BooleanField("Staff")
    is_graduate = models.BooleanField("Graduate Students")
    is_undergrad = models.BooleanField("Undergraduate Students")
    is_ra = models.BooleanField("Research Assistant")
    is_postdocs = models.BooleanField("Postdoctoral Researcher")
    is_alumni = models.BooleanField("Alumni")
    other = models.BooleanField("Other", default=None)

    def __str__(self):
        return '%s: %s %s ---%s' % (self.member_number, self.first_name, self.last_name, self.affiliation)

    class Meta:
        verbose_name = "Members"  # name in the admin site
        verbose_name_plural = verbose_name

