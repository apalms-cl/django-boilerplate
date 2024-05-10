import json

from django.http import JsonResponse
from django.conf import settings


def infoView(request, *args, **kwargs):
    with open(settings.BASE_DIR / "info.json", "r") as json_file:
        return JsonResponse(json.load(json_file))
