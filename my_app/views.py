from django.http import HttpResponse, HttpResponsePermanentRedirect
from my_site.restful.response import APIResponse, ErrorAPIResponse
from my_site.restful.views import APIViewSet
from my_app import models

# Create your views here.


def index(request):
    # response = HttpResponse()
    # response.write("<p>Here's the text of the Web page.</p>")
    # response.write("<p>Here's another paragraph.</p>")
    # return response

    return HttpResponsePermanentRedirect("https://www.djangoproject.com/")


def hi(request):
    return APIResponse({"message": "hello, world"})


def error(request):
    return ErrorAPIResponse("100000")


class Like(APIViewSet):
    model = models.Like


class History(APIViewSet):
    model = models.History
