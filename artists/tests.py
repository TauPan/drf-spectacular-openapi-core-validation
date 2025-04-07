import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from artists import models

pytestmark = [pytest.mark.django_db]

@pytest.fixture
def apiclient():
    return APIClient()


# pytestmark = [pytest.mark.django_db]
class TestArtistsList:

    def test_create(self, apiclient):
        response = apiclient.post(reverse("api:artists-list"),
                                  {'name': 'The Beatles',
                                   'country': 'GB'})
        assert response.status_code == 201
        assert models.Artist.objects.count() == 1
        artist = models.Artist.objects.get()
        assert artist.name == 'The Beatles'

    def test_create_unique(self, apiclient):
        self.test_create(apiclient)
        response = apiclient.post(reverse("api:artists-list"),
                                  {'name': 'The Beatles',
                                   'country': 'GB'})
        assert response.status_code == 400
        assert (response.json()['name']
                == ['artist with this name already exists.'])
