from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import APIKey

class APIKeyAuthentication(BaseAuthentication):
    """
    Authenticate requests using an 'x-api-key' header.
    """
    def authenticate(self, request):
        key = request.META.get('HTTP_X_API_KEY')
        if not key:
            return None  # no API key provided
        try:
            api_key = APIKey.objects.get(key=key, is_active=True)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed('Invalid or inactive API key')
        return (None, api_key)

    def authenticate_header(self, request):
        return 'x-api-key'