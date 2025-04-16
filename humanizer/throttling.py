from rest_framework.throttling import SimpleRateThrottle
from .models import APIKey

class APIKeyThrottle(SimpleRateThrottle):
    """
    Throttle based on the APIKey daily limit.
    """
    scope = 'apikey'

    def get_rate(self):
        key = self.request.META.get('HTTP_X_API_KEY')
        if not key:
            return None
        try:
            api = APIKey.objects.get(key=key)
        except APIKey.DoesNotExist:
            return None
        return f"{api.daily_limit}/day"

    def get_cache_key(self, request, view):
        key = request.META.get('HTTP_X_API_KEY')
        if not key:
            return None
        return self.cache_format % {'scope': self.scope, 'ident': key}