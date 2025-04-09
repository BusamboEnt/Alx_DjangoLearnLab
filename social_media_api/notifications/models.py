from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    recipient = models.ForeignKey(get_user_model(), related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(get_user_model(), related_name='acting_user', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)  # Describes the action, e.g., "liked", "commented on"
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # Mark if the notification has been read

    def __str__(self):
        return f"Notification for {self.recipient} by {self.actor}: {self.verb}"
