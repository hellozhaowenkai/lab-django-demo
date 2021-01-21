from django.http import JsonResponse


# Create your views here.


def hi(request):
    return JsonResponse({"message": "hello, world"})
