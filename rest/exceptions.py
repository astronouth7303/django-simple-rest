from django.http import HttpResponse


class HttpError(Exception):
    def __init__(self, message='Server Error', status=500):
        super(HttpError, self).__init__(message)
        self.status = status

    def __repr__(self):
        return 'HttpError(%r, %r)' % (self.status, self.message)


class ExceptionMiddleware(object):
    def process_exception(self, request, exception):
        """
        Returns the proper HttpRespone if an HttpError was thrown
        """
        response = None
        if isinstance(exception, HttpError):
            response = HttpResponse(
                content=exception.message,
                status=exception.status)
        return response