"""Apps."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """APIConfig."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
