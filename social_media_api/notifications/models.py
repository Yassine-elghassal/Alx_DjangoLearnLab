from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="actor_notifications")
    verb = models.CharField(max_length=255)  # Example: "liked your post", "followed you"
    
    # Generic relation to any model (e.g., Post, Comment)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('content_type', 'object_id')

    # **Missing timestamp field → ADD IT**
    timestamp = models.DateTimeField(auto_now_add=True)  # ✅ Fix: Add timestamp

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target}"
