from django.core.exceptions import FieldError
from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor
from django.db import models

import uuid


class APIModel(models.Model):
    """
    Intentionally simple parent class for all API models.
    """

    DISABLE_UPDATE_FIELDS = tuple(["uuid", "created_at"])
    AUTO_UPDATE_FIELDS = tuple(["last_modified_at"])

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def update(self, **kwargs):
        """Update the object based on the `kwargs` provided."""

        update_fields = [field for field in self.AUTO_UPDATE_FIELDS]
        for field, value in kwargs.items():
            if field in self.DISABLE_UPDATE_FIELDS:
                raise FieldError(f"The field {field} is a disable update field.")

            # models.ForeignKey
            # TODO: models.OneToOneField
            # TODO: models.ManyToManyField
            if isinstance(
                getattr(self._meta.concrete_model, field), ForwardManyToOneDescriptor
            ):
                field = f"{field}_id"

            setattr(self, field, value)
            update_fields.append(field)

        self.full_clean()
        self.save(update_fields=update_fields, force_update=True)

    def delete(self, using=None, keep_parents=False):
        """Delete the object by just set its `is_deleted` field to True."""

        self.update(is_deleted=True)

    class Meta:
        abstract = True
