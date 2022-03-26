from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.

class PostTest(TestCase):
    url = reverse('client')
    sender = APIClient()

    def test_post_good_client(self):
        
        data = {
            'phone_number': '79636660855',
            'operator_code': '963',
            'time_zone': '2',
            'tag': 'empty'
        }
        request = self.sender.post(self.url, data, format='json')
        
        assert request.status_code == 201

    def test_post_bad_client1(self):
        data = {
            'phone_number': '89636660855',
            'operator_code': '963',
            'time_zone': '2',
            'tag': 'empty'
        }
        request = self.sender.post(self.url, data, format='json')
        
        assert request.status_code == 400

    def test_post_bad_client2(self):
        data = {
            'phone_number': '777779636660855',
            'operator_code': '963',
            'time_zone': '2',
            'tag': 'empty'
        }
        request = self.sender.post(self.url, data, format='json')
        
        assert request.status_code == 400
