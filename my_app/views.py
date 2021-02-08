from my_site.restful.response import APIResponse, ErrorAPIResponse
from my_site.restful.views import APIViewSet
from my_app.models import LikeModel

# Create your views here.


def hi(request):
    return APIResponse({"message": "hello, world"})


def error(request):
    return ErrorAPIResponse("100100")


class LikeViewSet(APIViewSet):
    model = LikeModel
