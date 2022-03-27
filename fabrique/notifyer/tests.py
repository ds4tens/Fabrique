from django.urls import reverse
from notifyer import models
from rest_framework.test import APITestCase
from django.utils import timezone

# Create your tests here.

class ClientTest(APITestCase):
    url = reverse('client-list')

    def test_post_good_client2(self):
        
        data = {
            'phone_number': '79636660855',
            'operator_code': '963',
            'time_zone': 'Europe/Moscow',
            'tag': 'test'
        }
        request = self.client.post(self.url, data, format='json')
        
        assert request.status_code == 201
        self.assertEqual(models.Client.objects.count(), 1)

    def test_post_good_client2(self):
        
        data = {
            'phone_number': '79990989988',
            'operator_code': '999',
            'time_zone': 'Europe/Moscow',
            'tag': 'test'
        }
        request = self.client.post(self.url, data, format='json')
        
        assert request.status_code == 201
        self.assertEqual(models.Client.objects.count(), 1)
    
    def test_post_good_client3(self):
        
        data = {
            'phone_number': '77659087766',
            'operator_code': '765',
            'time_zone': 'Europe/Berlin',
            'tag': 'laman'
        }
        request = self.client.post(self.url, data, format='json')
        
        assert request.status_code == 201
        self.assertEqual(models.Client.objects.count(), 1)

    def test_post_bad_client1(self):
        data = {
            'phone_number': '89636660855',
            'operator_code': '963',
            'time_zone': 'Europe/London',
            'tag': 'empty'
        }
        request = self.client.post(self.url, data, format='json')
        
        assert request.status_code == 400

    def test_post_bad_client2(self):
        data = {
            'phone_number': '777779636660855',
            'operator_code': '963',
            'time_zone': '2',
            'tag': 'empty'
        }
        request = self.client.post(self.url, data, format='json')

        assert request.status_code == 400
    
    def test_client_list(self):
        data = {
            'phone_number': '77659087766',
            'operator_code': '765',
            'time_zone': 'Europe/Berlin',
            'tag': 'laman'
        }
        request = self.client.post(self.url, data, format='json')
        data = {
            'phone_number': '79636660855',
            'operator_code': '963',
            'time_zone': 'Europe/Moscow',
            'tag': 'test'
        }
        request = self.client.post(self.url, data, format='json')

        self.assertEqual(models.Client.objects.count(), 2)

class MailingTestCase(APITestCase):

    def test_post_good(self):
        url = reverse('mailing-list')
        data = {
            'content': 'test',
            'start_date': timezone.now()+timezone.timedelta(minutes=2),
            'finish_date': timezone.now()+timezone.timedelta(hours=2)
        }
        request = self.client.post(url, data, format='json')
        assert request.status_code == 400
    
    def test_wrong_time_format(self):
        url = reverse('mailing-list')
        data = {
            'content': 'test',
            'start_date': '12:34:11:2',
            'finish_date': timezone.now()+timezone.timedelta(hours=2)
        }
        request = self.client.post(url, data, format='json')
        assert request.status_code == 400
    
    def test_past_date(self):
        url = reverse('mailing-list')
        data = {
            'content': 'test',
            'start_date': timezone.now()+timezone.timedelta(minutes=2),
            'finish_date': timezone.now()-timezone.timedelta(hours=2)
        }
        request = self.client.post(url, data, format='json')
        assert request.status_code == 400