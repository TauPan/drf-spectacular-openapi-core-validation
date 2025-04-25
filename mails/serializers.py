from rest_framework.serializers import EmailField, ListField, ModelSerializer
import mails.models


class MailSerializer(ModelSerializer):
    from_addr = EmailField()  # aka Envelope-Address
    From = EmailField()       # From Header-Field
    To = ListField(child=EmailField(), allow_empty=False)

    class Meta:
        model = mails.models.Mail
        fields = '__all__'
