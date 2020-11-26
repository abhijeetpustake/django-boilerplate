from rest_framework.throttling import UserRateThrottle


class ClientRateThrottle(UserRateThrottle):
    """Custom class that implements throttling based on client_id or
    users ip address

    Args:
        UserRateThrottle (class): Extends UserRateThrottle base class
    """
    scope = 'client'

    def get_cache_key(self, request, view):
        if request.auth:
            ident = request.auth.application.client_id
        else:
            ident = self.get_ident(request)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }
