from django.db import models

class PhishResult(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} @ {self.submitted_at}"