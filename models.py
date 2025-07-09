from django.db import models
from django.contrib.auth.models import User

# Custom Manager to get unread notifications
class UnreadNotificationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_read=False)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Default manager
    objects = models.Manager()

    # Custom manager for unread
    unread = UnreadNotificationManager()

    def __str__(self):
        return f"{self.user.username} - {self.message[:50]}"
