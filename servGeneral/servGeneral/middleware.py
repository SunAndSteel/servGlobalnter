from django.http import HttpResponseForbidden

# Liste des plages d'adresses IP autorisées
ALLOWED_IP_RANGES = ["172.16.0.0/16", "172.17.0.0/16", "172.18.0.0/16", "172.19.0.0/16"]


class IPValidationMiddleware:
    """
    Middleware pour valider les adresses IP des requêtes entrantes.

    Ce middleware vérifie si l'adresse IP du client appartient à une
    plage d'adresses autorisées. Si ce n'est pas le cas, une réponse
    HTTP 403 (Forbidden) est retournée.

    Attributs :
        get_response (callable) : Fonction ou middleware suivant dans la chaîne de traitement.

    Méthodes :
        - __call__(request): Vérifie l'adresse IP et passe au middleware suivant si elle est valide.
        - get_client_ip(request): Extrait l'adresse IP de la requête HTTP.
    """

    def __init__(self, get_response):
        """
        Initialise le middleware avec la fonction de réponse suivante.

        Args:
            get_response (callable): Fonction ou middleware suivant dans la chaîne de traitement.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Traite chaque requête entrante. Vérifie si l'IP du client est autorisée.

        Args:
            request (HttpRequest): Objet représentant la requête HTTP.

        Returns:
            HttpResponse: Réponse HTTP appropriée (403 si l'IP n'est pas autorisée, sinon continue).
        """
        # Récupérer l'adresse IP du client
        client_ip = self.get_client_ip(request)

        # Vérifier si l'adresse IP appartient à une plage autorisée
        if not any(client_ip.startswith(allowed.split('/')[0]) for allowed in ALLOWED_IP_RANGES):
            # Retourner une réponse HTTP 403 si l'adresse IP n'est pas autorisée
            return HttpResponseForbidden("Forbidden: Access denied.")

        # Passer la requête au middleware suivant ou à la vue
        return self.get_response(request)

    def get_client_ip(self, request):
        """
        Récupère l'adresse IP du client à partir des en-têtes de la requête.

        L'adresse IP est obtenue à partir de l'en-tête `HTTP_X_FORWARDED_FOR` si
        un reverse proxy est utilisé, sinon elle est extraite de `REMOTE_ADDR`.

        Args:
            request (HttpRequest): Objet représentant la requête HTTP.

        Returns:
            str: Adresse IP du client.
        """
        # Vérifier si l'en-tête HTTP_X_FORWARDED_FOR est présent (cas de reverse proxy)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # Extraire la première adresse IP dans la liste
            ip = x_forwarded_for.split(',')[0]
        else:
            # Récupérer l'adresse IP depuis REMOTE_ADDR
            ip = request.META.get('REMOTE_ADDR')
        return ip
