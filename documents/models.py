from django.db import models
from django.contrib .auth.models import User
from users.models import User
import uuid


class Document(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        COMPLETED = 'Completed'
    
    # document_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    document_title = models.CharField(max_length=255)
    document_body = models.TextField()
    status = models.CharField(max_length=20, 
                              choices=StatusChoices.choices,
                              default=StatusChoices.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.document_title} by {self.owner.email}"
    
    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = "Documents"


class DocumentComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment for {self.document.document_title} by {self.user.email}"