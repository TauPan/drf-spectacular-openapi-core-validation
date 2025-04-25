from rest_framework.serializers import EmailField, ListField, ModelSerializer
import mails.models


class MailSerializer(ModelSerializer):
    To = ListField(child=EmailField(), allow_empty=False)

    class Meta:
        model = mails.models.Mail
        fields = '__all__'
