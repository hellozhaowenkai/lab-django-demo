from django.db import models
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.timezone import now

import json


class APIEncoder(DjangoJSONEncoder):
    """
    DjangoJSONEncoder subclass that knows how to encode QuerySet and Model.
    """

    def default(self, obj):
        if isinstance(
            obj,
            (
                models.QuerySet,
                models.Model,
            ),
        ):
            return self.jsonable(obj)

        return super().default(obj)

    @classmethod
    def jsonable(cls, obj):
        """The JavaScript Object Notation format support handler."""

        if isinstance(obj, models.Model):
            iterable = [obj]
            return cls.jsonable(iterable)[0]

        return json.loads(serialize("json", obj))


class APIResponse(JsonResponse):
    """
    An API response class that consumes `any data` to be serialized to JSON.
    """

    def __init__(self, data, *args, **kwargs):
        response_data = self.transform_response(data, *args, **kwargs)
        super().__init__(
            data=response_data,
            encoder=APIEncoder,
            safe=True,
            # json_dumps_params={"sort_keys": True},
        )

    @classmethod
    def transform_response(cls, data, *args, **kwargs):
        response_data = data
        return response_data


class ErrorAPIResponse(APIResponse):
    """
    An API response class that consumes `error info data` to be serialized to JSON.
    """

    ERROR_STATUS_CODE = {
        # DATABASE
        "100100": "NotFound: No target found matching the query.",
        "100101": "MultipleObjectsReturned: The query returned multiple objects when only one was expected.",
        "100102": "IntegrityError: The primary keys must be unique.",
        "100103": "FieldError: Some kind of problem with a model field.",
        "100104": "ValueError: Some fields do not exist in this model or are m2m fields.",
        "100105": "ValidationError: Enter a valid value.",
        # AUTHENTICATION
        "100200": "ValidationError: A user with that username already exists.",
        "100201": "PermissionDenied: The user did not have permission to do that.",
        # PAGINATION
        "100300": "InvalidPage: The requested page is invalid (i.e. not an integer) or contains no objects.",
    }

    @classmethod
    def transform_response(cls, data, *args, **kwargs):
        response_data = {
            # The error object.
            "error": {
                # One of a server-defined set of error codes.
                "code": data,
                # A human-readable representation of the error.
                "message": cls.ERROR_STATUS_CODE[data],
            }
        }
        return response_data


class CollectionAPIResponse(APIResponse):
    """
    An API response class that consumes `a list of objects data` to be serialized to JSON.
    """

    DEFAULT_PAGE_SIZE = 100
    DEFAULT_PAGE_NUMBER = 1

    @classmethod
    def transform_response(
        cls,
        data,
        page_size=DEFAULT_PAGE_SIZE,
        page_number=DEFAULT_PAGE_NUMBER,
    ):
        paginator = Paginator(data, page_size)
        page_obj = paginator.page(page_number)

        response_data = {
            # The total number of objects, across all pages.
            "count": page_obj.paginator.count,
            # The maximum number of items to include on a page.
            "per_page": page_obj.paginator.per_page,
            # The total number of pages.
            "num_pages": page_obj.paginator.num_pages,
            # A 1-based range iterator of page numbers, e.g. [1, 2, 3, 4].
            "page_range": [page for page in page_obj.paginator.page_range],
            # The previous page number.
            "previous": page_obj.previous_page_number()
            if page_obj.has_previous()
            else 0,
            # The 1-based page number for this page.
            "current": page_obj.number,
            # The next page number.
            "next": page_obj.next_page_number() if page_obj.has_next() else 0,
            # The 1-based index of the first object on the page, relative to all of the objects in the paginator’s list.
            "start_index": page_obj.start_index(),
            # The 1-based index of the last object on the page, relative to all of the objects in the paginator’s list.
            "end_index": page_obj.end_index(),
            # The list of objects on this page.
            "result": page_obj.object_list,
        }
        return response_data


class ItemAPIResponse(APIResponse):
    """
    An API response class that consumes `a single object` data to be serialized to JSON.
    """

    @classmethod
    def transform_response(cls, data, *args, **kwargs):
        response_data = {
            "result": data,
        }
        return response_data


class OperationAPIResponse(APIResponse):
    """
    An API response class that consumes `operation info data` to be serialized to JSON.
    """

    @classmethod
    def transform_response(
        cls,
        data,
        created_at=None,
        last_action_at=None,
        percent_complete=100,
        status="succeeded",
        *args,
        **kwargs
    ):
        response_data = {
            # The datetime when the operation was created.
            "created_at": created_at or now(),
            # The datetime for when the current state was entered.
            "last_action_at": last_action_at or now(),
            # Sometimes it is impossible for services to know with any accuracy when an operation will complete.
            "percent_complete": percent_complete,
            # Operations MUST support the following states: [not_started | running | succeeded | failed].
            "status": status,
            # The result of the operation.
            "result": data,
        }
        return response_data
