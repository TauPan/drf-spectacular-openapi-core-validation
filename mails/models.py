from django.db import models

# Create your models here.
class Mail(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    from_addr = models.TextField()
    Subject = models.TextField(null=True)
    From = models.TextField(null=True)
    To = models.JSONField(null=True)
    extra_headers = models.JSONField(null=True)
    mail_body = models.TextField(null=True)
    attachments = models.JSONField(null=True)
