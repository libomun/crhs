from allauth.account.signals import user_signed_up
from django.core.mail import send_mail
from django.dispatch import receiver


@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):
    send_mail(
        'New User Registered in Rural360',
        'A new user has signed up in Rural360.\n\n'
        'Name: {} {}\n'
        'Email Address: {}\n\n'
        'Please go to the website (www.rural360.com) to manage this user.'.format(user.first_name, user.last_name, user.email),
        'ruraldex@gmail.com',  # replace this with your own email
        ['ruraldex@gmail.com'],
        fail_silently=False,
    )
