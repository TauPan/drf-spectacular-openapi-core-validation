from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from mails import models, serializers


class MailViewSet(ModelViewSet):
    model = models.Mail
    queryset = models.Mail.objects.all()
    serializer_class = serializers.MailSerializer
