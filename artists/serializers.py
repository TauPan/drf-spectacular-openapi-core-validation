from rest_framework.serializers import ModelSerializer
import artists.models


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = artists.models.Artist
        fields = '__all__'
