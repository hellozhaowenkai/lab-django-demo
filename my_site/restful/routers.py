from django.urls import path, re_path, include


class APIRouter:
    """
    The RESTful style API Router.
    """

    base_urls = {
        "": {
            "get": "list",
            "post": "create",
        },
        "<int:pk>/": {
            "get": "detail",
            "put": "update_or_create",
            "patch": "update",
            "delete": "drop",
        },
        "<uuid:uuid>/": {
            "get": "detail",
            "put": "update_or_create",
            "patch": "update",
            "delete": "drop",
        },
    }

    def __init__(self, prefix, view_set):
        self.prefix = prefix
        self.view_set = view_set
        self.patterns = []

        for url, actions in self.base_urls.items():
            self.register(url, actions)

    @property
    def urls(self):
        return path(self.prefix, include(self.patterns))

    def register(self, url, actions):
        """The RESTful style URL register."""

        self.patterns.append(
            path(
                url,
                self.view_set.as_view(actions=actions),
            )
        )
