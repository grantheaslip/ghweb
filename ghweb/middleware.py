from django.shortcuts import redirect
from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

# Adapted from https://github.com/etianen/django-herokuapp/blob/bd0a5d6af08f4d5f90b202bb6be1494b1a9850e1/herokuapp/middleware.py
class CanonicalSchemeAndHostMiddleware(object):
    """Middleware that redirects to a canonical scheme and host."""

    def __init__(self, get_response):
        self.get_response = get_response

        if not (settings.CANONICAL_SCHEME and settings.CANONICAL_HOST):
            logger.warning(
                'CanonicalSchemeAndHostMiddleware disabled because ' +
                'CANONICAL_SCHEME and/or CANONICAL_HOST missing'
            )
            raise MiddlewareNotUsed

    def __call__(self, request):
        request_scheme = request.META.get(
            "HTTP_X_FORWARDED_PROTO",
            request.scheme
        )
        request_host = request.get_host()

        if (
            (
                request_scheme == settings.CANONICAL_SCHEME and
                request_host == settings.CANONICAL_HOST
            )
            or 'localhost' in request_host
        ):
            return self.get_response(request)
        else:
            canonical_url = (
                settings.CANONICAL_SCHEME + '://' +
                settings.CANONICAL_HOST +
                request.get_full_path()
            )
            logger.info(
                'Triggering canonical redirect from ' +
                request.build_absolute_uri() +
                ' to ' +
                canonical_url
            )

            # TODO: Change permanent to True once tested
            return redirect(canonical_url, permanent=False)


class ExceptionLoggingMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        logger.exception(
            'Unhandled exception while rendering "' +
            request.path +
            '":'
        )
