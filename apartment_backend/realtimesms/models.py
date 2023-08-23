from django.contrib.auth.models import User
from django.db import models

from apartment_backend.apartment.models import PropertyInquiry, PropertyBooking


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    inquiry = models.ForeignKey(PropertyInquiry, on_delete=models.CASCADE, null=True, blank=True)
    booking = models.ForeignKey(PropertyBooking, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"
