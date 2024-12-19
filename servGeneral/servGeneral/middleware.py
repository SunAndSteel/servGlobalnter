from django.http import HttpResponseForbidden
from django.shortcuts import redirect


ALLOWED_IP_RANGES = ["172.16.0.0/16", "172.17.0.0/16", "172.18.0.0/16", "172.19.0.0/16"]


class IPValidationMiddleware:
    """
    Validation par IP, vérifier que l’user a une IP autorisée.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        client_ip = self.get_client_ip(request)
        if not any(client_ip.startswith(allowed) for allowed in self.ALLOWED_IP_RANGES):
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("Forbidden")
        return self.get_response(request)

    def get_client_ip(self, request):

        """
        Récupère l'adressse à partir de l'entête REMOTE_ADDR ou
        HTTP_X_FORWARDED_FOR. (reverse-proxy ou navigateur)
        returns: str
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

