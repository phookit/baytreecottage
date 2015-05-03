# foo/apps.py

from django.apps import AppConfig

class PaginatorConfig(AppConfig):
    name = 'phookit.core'
    label = 'my.phookit.core'


default_app_config = 'phookit.core.PaginatorConfig'

