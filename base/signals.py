from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactSubmission

@receiver(post_save, sender=ContactSubmission)
def send_contact_confirmation(sender, instance, created, **kwargs):
    if created:
        subject = "Thank you for contacting us!"
        message = (
            f"Hi {instance.name},\n\n"
            "Thank you for reaching out. We have received your message and will get back to you shortly.\n\n"
            "Best regards,\n"
            "Your Company Team"
        )
        recipient_list = [instance.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
