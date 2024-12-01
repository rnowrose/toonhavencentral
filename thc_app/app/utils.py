import builtins
import hashlib
import json
import re
from datetime import datetime
from decimal import Decimal


def generate_fake_checksum(value):
    return hashlib.md5(value.encode()).hexdigest()


EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")


def is_valid_email(email):
    return EMAIL_REGEX.fullmatch(email) != None


def safe_percent(nom, denom, places=2):
    return builtins.round(100 * nom / denom, places) if denom else 0


def json_loads(s):
    return json.loads(s)


def get_request_json(request):
    return json.loads(request.body.decode("utf-8"))


def json_dumps(obj):
    def _handler(obj):
        if hasattr(obj, "isoformat"):
            return obj.isoformat()
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            raise TypeError(
                "Object of type %s with value of %s is not JSON serializable"
                % (type(obj), repr(obj))
            )

    return json.dumps(obj, default=_handler)
