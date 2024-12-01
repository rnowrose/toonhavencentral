import logging
from django.http import HttpResponseBadRequest, HttpResponseServerError, JsonResponse
from ninja import Form, Router
from django.contrib import auth
from ninja.security import django_auth
from ninja_jwt.tokens import RefreshToken
from ninja.errors import HttpError


from app.dto.user import NewUser, TokenSchema, UserLogin
from services import user
from thc_app.app.exceptions import InvalidUserEmail, UserAlreadyExists


user_api = Router()
logger = logging.getLogger(__name__)


@user_api.get("/api-example")
def example_view(request):
    return {"message": "Hello, Ninja API!"}


@user_api.post("/login", response=TokenSchema)
def api_login(request, user: UserLogin):
    user = auth.authenticate(username=user.username, password=user.password)
    if not user:
        raise HttpError(401, "Invalid username or password")
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')[:50]
        logger.warning(f'failed login attempt: {ip_address:20}, {email}')

    # Generate tokens for the authenticated user
    refresh = RefreshToken.for_user(user)
    access = refresh.access_token

    return {"access": str(access), "refresh": str(refresh)}

@user_api.post("/register", response=NewUser)
def api_signup(request, new_user:Form[NewUser]):
    try:
        return user.create_user(new_user.dict())
    except (KeyError, ValueError, TypeError) as e:
        logger.error("%s: %s", type(e), e)
        return HttpResponseBadRequest()
    except InvalidUserEmail as e:
        logger.warning("%s: %s", type(e), e)
        return HttpResponseBadRequest()
    except UserAlreadyExists as e:
        logger.warning("%s: %s", type(e), e)
        return HttpError(409, "User Already Exist")  # Conflict
    except Exception:
        logger.exception('error during signup')
        return HttpResponseServerError()
