from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from artists import models
from artists import serializers

class ArtistViewSet(ModelViewSet):
    model = models.Artist
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer
