from urllib.parse import urlencode

from django.conf import settings


def generate_url(type, path, query={}):
    # FIXME(update): Update this logic for your hunt
    host = {
        "prehunt": settings.PREHUNT_HOST,
        "hunt": settings.HUNT_HOST,
        "registration": settings.REGISTRATION_HOST,
        "internal": settings.HUNT_HOST,
    }[type]
    assert host is not None
    path = path.lstrip("/")
    base_url = f"https://{host}/{path}"
    if not query:
        return base_url

    return f"{base_url}?{urlencode(query)}"
