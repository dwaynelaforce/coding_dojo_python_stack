from django.db import models
from main_app.models import User

# Create your models here.
class PostedMessage(models.Model):
    content = models.TextField(max_length=2045)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField(max_length=2045)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    postedmessage = models.ForeignKey(PostedMessage, related_name="comments", on_delete=models.CASCADE)
