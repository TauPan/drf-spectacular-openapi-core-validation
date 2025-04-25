from rest_framework.serializers import ModelSerializer
import mails.models


class MailSerializer(ModelSerializer):
    class Meta:
        model = mails.models.Mail
        fields = '__all__'
