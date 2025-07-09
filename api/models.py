from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions')
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Session {self.id} by {self.user.username}"

class Media(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='media/')
    media_type = models.CharField(max_length=10, choices=(('image', 'Image'), ('audio', 'Audio')))
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.media_type} for Session {self.session.id}"

class Note(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='notes')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for Session {self.session.id}" 