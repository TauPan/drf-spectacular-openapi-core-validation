from rest_framework.serializers import DictField, EmailField, ListField, ModelSerializer
import mails.models


# An Attachment Object is a dictionary with the following keys:
#   filename:   filename without path
#   binary:     true or false
#   media_type: a valid media type
#   content:    valid content fitting the media type
#               (utf-8 for non-binary or base64 for binary)
#
# Example:
# {
# "filename": "foo.txt",
# "binary": false,
# "media_type": "text/plain",
# "content": "Hello World!"
# }
class AttachmentField(DictField):
    pass


class MailSerializer(ModelSerializer):
    To = ListField(child=EmailField(max_length=254), allow_empty=False)
    attachment = ListField(child=AttachmentField(), allow_empty=True)

    class Meta:
        model = mails.models.Mail
        fields = '__all__'
