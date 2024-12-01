from django.db import models

class UserMessage(models.Model):
    user_id = models.BigIntegerField()
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

