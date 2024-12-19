from django.http import HttpResponseForbidden
from django.shortcuts import redirect


ALLOWED_IP_VLAN10 = "172.16.0.0/16"
ALLOWED_IP_VLAN20 = "172.17.0.0/16"
ALLOWED_IP_VLAN30 = "172.18.0.0/16"
ALLOWED_IP_VLAN40 = "172.19.0.0/16"


class IPValidationMiddleware:
    """
    Validation par IP, vérifier que l’user a une IP dans le bon VLAN.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        client_ip = self.get_client_ip(request)

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