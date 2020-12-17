from django.contrib import admin
from django.apps import apps

filesystem = apps.get_app_config('filesystem')
admin.site.register(filesystem.get_models())
