from ipware import get_client_ip
from django.http import HttpResponseForbidden
import logging
from django.conf import settings
logger = logging.getLogger(__name__)


class MEISOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip, is_routable = get_client_ip(request)
        if client_ip is None:
            logger.warn('Vietato l\'accesso all\'IP perchè è nullo')
            return HttpResponseForbidden()
        if client_ip in settings.ALLOWED_IPS:
                response = self.get_response(request)
                return response
        logger.warn(f'Vietato l\'accesso all\'IP {client_ip} perchè non autorizzato')
        return HttpResponseForbidden()

 
 