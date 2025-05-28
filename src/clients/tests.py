from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Client

class ClientTests(APITestCase):
    def setUp(self):
        self.client_data = {
            'nom': 'Doe',
            'prenom': 'John',
            'email': 'john.doe@example.com',
            'telephone': '1234567890',
            'adresse': '123 Main St',
            'statut': 'active',
            'IFU': '123456789',
            'RCCM': '987654321'
        }

    def test_create_client(self):
        response = self.client.post(reverse('client-list'), self.client_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().nom, 'Doe')

    def test_get_client(self):
        client = Client.objects.create(**self.client_data)
        response = self.client.get(reverse('client-detail', args=[client.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nom'], client.nom)

    def test_update_client(self):
        client = Client.objects.create(**self.client_data)
        updated_data = {'nom': 'Smith'}
        response = self.client.put(reverse('client-detail', args=[client.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.refresh_from_db()
        self.assertEqual(client.nom, 'Smith')

    def test_delete_client(self):
        client = Client.objects.create(**self.client_data)
        response = self.client.delete(reverse('client-detail', args=[client.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Client.objects.count(), 0)