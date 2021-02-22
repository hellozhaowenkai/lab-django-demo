from my_site.restful.response import APIResponse, ErrorAPIResponse
from my_site.restful.views import APIViewSet
from my_app import models

# Create your views here.


def hi(request):
    return APIResponse({"message": "hello, world"})


def error(request):
    return ErrorAPIResponse("100100")


class Like(APIViewSet):
    model = models.Like


class History(APIViewSet):
    model = models.History
