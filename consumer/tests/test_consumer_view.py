from django.test import TestCase
from rest_framework.test import APIClient
from consumer.models.consumer import ConsumerStatusType
from consumer.tests.factories import ConsumerFactory


class TestConsumerView(TestCase):
    def setUp(self):
        self.client = APIClient()
        pass

    def test_consumer_collection_filtering(self):
        consumer1 = ConsumerFactory(previous_jobs_count=1, status=ConsumerStatusType.active)
        consumer2 = ConsumerFactory(previous_jobs_count=1, status=ConsumerStatusType.in_progress)
        consumer3 = ConsumerFactory(previous_jobs_count=3, status=ConsumerStatusType.collected)

        # all consumers
        response = self.client.get(
            f"/consumers/"
        )
        assert response.status_code == 200
        assert len(response.data["results"]["features"]) == 3

        # filter by status
        response = self.client.get(
            f"/consumers/?status={ConsumerStatusType.collected.value}"
        )
        assert response.status_code == 200
        assert len(response.data["results"]["features"]) == 1
        assert response.data["results"]["features"][0]['properties']['id'] == consumer3.id


        # filter by previous_jobs_count
        response = self.client.get(
            f"/consumers/?previous_jobs_count=1"
        )
        assert response.status_code == 200
        assert len(response.data["results"]["features"]) == 2
        assert response.data["results"]["features"][0]['properties']['id'] == consumer1.id
        assert response.data["results"]["features"][1]['properties']['id'] == consumer2.id

        print(response.data)
