import logging
from django.utils.deprecation import MiddlewareMixin
from ninja_jwt.authentication import JWTAuth

logger = logging.getLogger(__name__)

class LogJWTMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if there's a valid JWT in the Authorization header
        auth = JWTAuth()
        user = auth.authenticate(request)
        if user:
            request.user = user[0]  # Set the user object

        # Log JWT usage
        if hasattr(request, "user") and request.user.is_authenticated:
            logger.info(f"Authenticated user: {request.user.username}")
