# Importation des classes nécessaires de Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importation des modèles et serializers
from .models import LocalUpdate
from .serializers import LocalUpdateSerializer


class LocalUpdateAPIView(APIView):
    """
    APIView permettant de gérer la création d'une mise à jour locale via une requête POST.

    Cette vue reçoit des données au format JSON, les valide à l'aide du serializer
    `LocalUpdateSerializer`, et sauvegarde les données si elles sont valides.

    Méthodes :
        - post(request): Gère la requête POST pour créer une mise à jour locale.
    """

    def post(self, request):
        """
        Gère une requête POST pour créer une nouvelle mise à jour locale.

        Args:
            request (Request): Requête HTTP contenant les données de la mise à jour locale.

        Returns:
            Response: Réponse HTTP contenant les données validées et sauvegardées
                        (statut HTTP 201 si succès) ou les erreurs de validation
                        (statut HTTP 400 en cas d'échec).
        """
        # Sérialiser les données envoyées dans la requête
        serializer = LocalUpdateSerializer(data=request.data)

        # Valider les données du serializer
        if serializer.is_valid():
            # Si les données sont valides, les sauvegarder dans la base de données
            serializer.save()

            # Retourner les données validées avec un statut HTTP 201 (créé)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Si les données sont invalides, retourner les erreurs avec un statut HTTP 400 (mauvaise requête)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
