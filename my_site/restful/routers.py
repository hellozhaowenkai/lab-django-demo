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

    def __init__(self, view_set):
        self.view_set = view_set
        self.verbose_name = view_set.get_verbose_name()
        self.verbose_name_plural = view_set.get_verbose_name_plural()
        self.patterns = []
        self.sub_patterns = []

        for url, actions in self.base_urls.items():
            self.register(url, actions)

    @property
    def urls(self):
        self.patterns.append(
            path(f"<int:{self.verbose_name}_id>/", include(self.sub_patterns))
        )
        self.patterns.append(
            path(f"<uuid:{self.verbose_name}__uuid>/", include(self.sub_patterns))
        )
        return path(f"{self.verbose_name_plural}/", include(self.patterns))

    def register(self, url, actions):
        """The RESTful style URL register."""

        self.patterns.append(
            path(
                url,
                self.view_set.as_view(actions=actions),
            )
        )

    def add_sub_routers(self, *sub_routers):
        self.sub_patterns.extend([sub_router.urls for sub_router in sub_routers])
