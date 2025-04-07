import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

@pytest.fixture
def apiclient():
    return APIClient()


# pytestmark = [pytest.mark.django_db]
class TestArtistsList:

    def test_create(self, apiclient):
        response = apiclient.post(reverse("api:artists"),
                                  {'name': 'The Beatles'})
        assert response.status_code == 201
