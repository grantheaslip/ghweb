import personal
from django.core.exceptions import ImproperlyConfigured
from importlib import import_module
from pprint import pprint

def app_name_and_version(request):
    if request.resolver_match.app_name == '':
        raise ImproperlyConfigured('This app’s URLconf has no app_name attribute')

    current_app_module = import_module(request.resolver_match.app_name)
    if not hasattr(current_app_module, '__version__'):
        raise ImproperlyConfigured('This app’s module has no __version__ attribute')

    current_app_name = request.resolver_match.app_name
    current_app_version = current_app_module.__version__

    return {
        'app_name_and_version': f"ghweb.{current_app_name} {current_app_version}",
    }
