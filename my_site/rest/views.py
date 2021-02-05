from django.db import IntegrityError
from django.core.paginator import InvalidPage
from django.http import Http404
from django.core.exceptions import FieldError, ValidationError, MultipleObjectsReturned

from django.http.request import validate_host
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from django.conf import settings
from my_site.rest.response import (
    APIResponse,
    ErrorAPIResponse,
    ItemAPIResponse,
    CollectionAPIResponse,
    OperationAPIResponse,
)

import json


class APIBaseView:
    """
    Intentionally simple parent class for all API views.
    """

    CORS_ALLOWED_ORIGINS = tuple(settings.ALLOWED_HOSTS)
    CORS_BLOCKED_ORIGINS = tuple([])

    slug_field = "uuid"

    @classmethod
    def corsable(cls, response, request):
        """The Cross-Origin Resource Sharing request support handler"""

        # Indicates where a fetch originates from.
        origin = request.headers.get("Origin")

        if (origin is not None) and (
            validate_host(origin, cls.CORS_ALLOWED_ORIGINS)
            and not validate_host(origin, cls.CORS_BLOCKED_ORIGINS)
        ):
            # Indicates whether the response can be shared.
            response["Access-Control-Allow-Origin"] = origin
            # Indicates whether or not the response to the request can be exposed when the credentials flag is true.
            response["Access-Control-Allow-Credentials"] = "true"
            # Indicates which headers can be exposed as part of the response by listing their names.
            response["Access-Control-Expose-Headers"] = "true"

            if request.method == "OPTIONS":
                # Indicates how long the results of a preflight request can be cached.
                response["Access-Control-Max-Age"] = "3600"

                # Used when issuing a preflight request to let the server know
                #   which HTTP headers will be used when the actual request is made.
                request_method = request.headers.get(
                    "Access-Control-Request-Method", ""
                )
                # Specifies the method or methods allowed
                #   when accessing the resource in response to a preflight request.
                response["Access-Control-Allow-Methods"] = request_method
                # Used when issuing a preflight request to let the server know
                #   which HTTP method will be used when the actual request is made.
                request_headers = request.headers.get(
                    "Access-Control-Request-Headers", ""
                )
                # Used in response to a preflight request to indicate
                #   which HTTP headers can be used when making the actual request.
                response["Access-Control-Allow-Headers"] = request_headers

            # To indicate to clients that server responses will differ based on the value of the Origin request header.
            response["Vary"] = "Origin"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """Try to dispatch to the right method."""

        try:
            response = super().dispatch(request, *args, **kwargs)
            self.corsable(response, request)
            return response
        except Http404:
            error_response = ErrorAPIResponse("100100")
            error_response.status_code = 404
            return error_response
        except MultipleObjectsReturned:
            return ErrorAPIResponse("100101")
        except IntegrityError:
            return ErrorAPIResponse("100102")
        except FieldError:
            return ErrorAPIResponse("100103")
        except ValueError:
            return ErrorAPIResponse("100104")
        except ValidationError:
            return ErrorAPIResponse("100105")
        except InvalidPage:
            return ErrorAPIResponse("100300")

    def head(self, request, *args, **kwargs):
        """Return metadata of the result for a GET response."""

        response = self.get(self, request, *args, **kwargs)
        if not response.streaming and not response.has_header("Content-Length"):
            response["Content-Length"] = str(len(response.content))
        response.content = ""
        return response

    def options(self, request, *args, **kwargs):
        """Get information about a request."""

        return super().options(self, request, *args, **kwargs)


class APIListView(APIBaseView, BaseListView):
    """
    A base API view for displaying a list of objects.
    """

    DEFAULT_PAGE_SIZE = 100
    DEFAULT_PAGE_NUMBER = 1
    DEFAULT_ORDER_BY = "pk"

    def get(self, request, *args, **kwargs):
        """Return the current paginated collection value of multiple objects."""

        page_size = request.GET.get("size") or self.DEFAULT_PAGE_SIZE
        page_number = request.GET.get("page") or self.DEFAULT_PAGE_NUMBER
        order_by = request.GET.get("order_by") or self.DEFAULT_ORDER_BY

        queryset = self.get_queryset()
        ordered_queryset = queryset.order_by(order_by)
        return CollectionAPIResponse(
            ordered_queryset, page_size=page_size, page_number=page_number
        )

    def post(self, request, *args, **kwargs):
        """Create a new object based on the data provided, or submit a command."""

        new_object = self.model.objects.create()
        return OperationAPIResponse(new_object)


class APIDetailView(APIBaseView, BaseDetailView):
    """
    A base API view for displaying a single object.
    """

    def get(self, request, *args, **kwargs):
        """Return the current value of an object."""

        target_object = self.get_object()
        return ItemAPIResponse(target_object)

    def patch(self, request, *args, **kwargs):
        """Apply a partial update to an object."""

        data = json.loads(request.body)
        target_object = self.get_object()
        target_object.update(**data)
        return OperationAPIResponse(target_object)

    def put(self, request, *args, **kwargs):
        """Replace an object, or create a named object, when applicable."""

        data = json.loads(request.body)

        try:
            target_object = self.get_object()
        except Http404:
            target_object = self.model.objects.create(**kwargs)
        target_object.update(**data)

        return OperationAPIResponse(target_object)

    def delete(self, request, *args, **kwargs):
        """Delete an object."""

        target_object = self.get_object()
        target_object.delete()
        return OperationAPIResponse(target_object)
