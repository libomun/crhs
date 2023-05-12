from django.db import models

# Customizing user model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# # Email notification
# from django.contrib.admin.models import LogEntry
# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
#
# # Email notification for log entry
# @receiver(post_save, sender=LogEntry)
# def send_notification_email(sender, instance, created, **kwargs):
#     if created:
#         user = instance.user if instance.user else "no user given"
#         content_type = instance.content_type if instance.content_type else "no content_type given"
#         change_message = instance.change_message if instance.change_message else 'no change_message'
#
#         subject = 'rural360 Log '
#         message = 'A new notification from rural360!\n'
#         message += 'USER: ' + str(user) + '\n' + 'CONTENT TYPE: ' + str(content_type) + '\n' + 'CHANGE MESSAGE: ' + str(change_message) + '\n'
#         message += '--' * 30
#         send_mail(
#             subject,
#             message,
#             'liboliu186@gmail',
#             ['liulibo186@163.com'],
#             fail_silently=False,
#         )

