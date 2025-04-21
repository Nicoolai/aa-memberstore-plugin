"""App Configuration"""

# Django
from django.apps import AppConfig

# AA Example App
from memberstore import __version__


class MemberstoreConfig(AppConfig):
    """App Config"""

    name = "memberstore"
    label = "memberstore"
    verbose_name = f"Memberstore App v{__version__}"
