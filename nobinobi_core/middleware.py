from django.http import Http404
from django.urls import reverse


class RestrictStaffToAdminMiddleware():
    """
    A middleware that restricts staff members access to administration panels.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path.startswith(reverse('admin:index')):
            if request.user.is_authenticated():
                if not request.user.is_staff:
                    raise Http404
            else:
                raise Http404
        # Code to be executed for each request/response after
        # the view is called.
