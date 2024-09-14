from django.db import models
from django.conf import settings

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.file.name

class HtmlContent(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_file = models.ForeignKey(UploadedFile, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='html_contents')