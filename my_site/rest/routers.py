from django.urls import path, re_path, include


class APIRouter:
    """
    The RESTful style API Router.
    """

    def __init__(self, prefix):
        self.prefix = prefix

    def register(self, list_view_class, detail_view_class):
        """The RESTful style URL register."""

        patterns = [
            path("", list_view_class.as_view()),
            path("<int:pk>/", detail_view_class.as_view()),
            path("<uuid:slug>/", detail_view_class.as_view()),
        ]
        return path(self.prefix, include(patterns))
