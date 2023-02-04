from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Annonce, BienImmobilier, TypeAnnonce, Contact, Wilaya, Commune, CategorieAnnonce

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
#Ce code teste différents scénarios de filtrage des résultats. Le cas où tous les champs sont spécifiés, le cas où aucun champ n'est spécifié, et le cas où seulement certains champs sont spécifiés. Les assertions vérifient que la réponse renvoyée par la fonction a le bon statut HTTP et le bon nombre d'objets retournés.
class FirstFunctionTestCase(APITestCase):
    def setUp(self):
        # Create a few test objects in the database
        ...

    def test_filter_results_all_fields_specified(self):
        # Set up the data for the request
        data = {'type_id': 1, 'wilaya_id': 2, 'commune_id': 3, 'date_1': '2022-01-01', 'date_2': '2022-12-31'}
        url = reverse('firstFunction')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one object should match the filters

    def test_filter_results_no_fields_specified(self):
        data = {}
        url = reverse('firstFunction')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # All objects should be returned

    def test_filter_results_some_fields_specified(self):
        data = {'type_id': 1, 'date_1': '2022-01-01', 'date_2': '2022-12-31'}
        url = reverse('firstFunction')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two objects should match the filters


from django.test import TestCase
from rest_framework import status
import json

class CreateAnnonceTest(TestCase):
    def setUp(self):
        # setup the data for the test
        self.valid_payload = {
            "bienImmobilier": 1,
            "type": 1,
            "description": "Test description",
            "prix": 100000,
            "date": "2022-01-01"
        }
        self.invalid_payload = {
            "bienImmobilier": 1,
            "type": "",
            "description": "Test description",
            "prix": 100000,
            "date": "2022-01-01"
        }

    def test_create_valid_annonce(self):
        response = self.client.post(
            '/api/annonces/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_annonce(self):
        response = self.client.post(
            '/./views.py/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#test unitaire pour supprimer annonce
from django.test import Client, TestCase
from django.urls import reverse

class DeleteAnnonceTestCase(TestCase):

    def setUp(self):
        # Création de l'annonce pour la supprimer par la suite
        self.annonce = Annonce.objects.create(
            # ... informations de l'annonce ...
        )
        self.client = Client()

    def test_delete_annonce(self):
        # Envoi de la requête DELETE pour supprimer l'annonce
        response = self.client.delete(reverse('annonces:annonce-detail', kwargs={'pk': self.annonce.id}))

        # Vérification de la réponse
        self.assertEqual(response.status_code, 204) # 204 signifie "No Content" et indique que la requête a été exécutée avec succès, mais sans réponse à renvoyer
        self.assertFalse(Annonce.objects.filter(pk=self.annonce.id).exists())
#test unitaire pour search feature