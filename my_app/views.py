from my_site.rest.response import APIResponse, ErrorAPIResponse
from my_site.rest.views import APIListView, APIDetailView
from my_app.models import LikeModel

# Create your views here.


def hi(request):
    return APIResponse({"message": "hello, world"})


def error(request):
    return ErrorAPIResponse("100100")


class LikeListView(APIListView):
    model = LikeModel
    queryset = model.objects.exclude(is_deleted=True)


class LikeDetailView(APIDetailView):
    model = LikeModel
