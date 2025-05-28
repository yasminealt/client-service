from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from .models import Client
from .serializers import ClientSerializer

class ClientListCreateView(generics.ListCreateAPIView):
    """
    Vue pour lister et créer des clients
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @swagger_auto_schema(
        operation_summary="Liste des clients",
        operation_description="Récupère la liste de tous les clients",
        responses={
            200: ClientSerializer(many=True),
            400: "Requête invalide",
            500: "Erreur serveur"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Création d'un client",
        operation_description="Crée un nouveau client dans le système",
        request_body=ClientSerializer,
        responses={
            201: ClientSerializer(),
            400: "Données invalides",
            500: "Erreur serveur"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vue pour gérer un client spécifique
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @swagger_auto_schema(
        operation_summary="Détails d'un client",
        operation_description="Récupère les informations détaillées d'un client",
        responses={
            200: ClientSerializer(),
            404: "Client non trouvé",
            500: "Erreur serveur"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Modification d'un client",
        operation_description="Met à jour les informations d'un client existant",
        request_body=ClientSerializer,
        responses={
            200: ClientSerializer(),
            400: "Données invalides",
            404: "Client non trouvé",
            500: "Erreur serveur"
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Suppression d'un client",
        operation_description="Supprime un client du système",
        responses={
            204: "Client supprimé avec succès",
            404: "Client non trouvé",
            500: "Erreur serveur"
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)