from django.contrib import admin
from django.db import models

# Create your models here.
class Mail(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    from_addr = models.EmailField()
    Subject = models.TextField(null=True)
    From = models.EmailField(null=True)
    To = models.JSONField(null=True)
    extra_headers = models.JSONField(null=True)
    mail_body = models.TextField(null=True)
    attachments = models.JSONField(null=True)


admin.site.register(Mail)
