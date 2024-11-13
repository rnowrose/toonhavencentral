from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def example_test(request):
    usernames = {}
    try:
        # Retrieve a user by username
        user = User.objects.get(username='rownoknowrose')
        usernames = {
            "id": user.id,
            "username": user.username
        }
    except ObjectDoesNotExist:
        print("User does not exist.")
    except MultipleObjectsReturned:
        print("Multiple users returned.")

    return JsonResponse(usernames)
