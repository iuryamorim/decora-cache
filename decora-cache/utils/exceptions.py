# -*- coding: utf-8 -*-
"""Exception File"""


class ParserException(Exception):
    """Formatting fail exception"""

    def __init__(self, message=None):
        if not message:
            message = u"Object formatting fail."
        super(ParserException, self).__init__(message)


class ValidationException(Exception):
    """Validation fail exception"""

    def __init__(self, message=None):
        if not message:
            message = u"Object validation fail."
        super(ValidationException, self).__init__(message)


class NotACallableException(Exception):
    """Not a callable object exception"""

    def __init__(self, message=None):
        if not message:
            message = u"This not a callable object."
        super(NotACallableException, self).__init__(message)


class RequestException(Exception):
    """Request fail exception"""

    def __init__(self, message=None):
        if not message:
            message = u"Fail when making the request."
        super(RequestException, self).__init__(message)


class RequiredAttributeException(Exception):
    """Required attribute not found exception"""

    def __init__(self, message=None):
        if not message:
            message = u"An required attribute could not found."
        super(RequiredAttributeException, self).__init__(message)


class HttpException(Exception):
    """Http connection fail exception"""

    def __init__(self, message=None):
        if not message:
            message = u"HTTP connection Fail."
        super(HttpException, self).__init__(message)


class ConnectionException(Exception):
    """Connection fail exception"""

    def __init__(self, message=None):
        if not message:
            message = u"Failed connect to server."
        super(ConnectionException, self).__init__(message)


class TimeOutException(Exception):
    """TimeOut exception"""

    def __init__(self, message=None):
        if not message:
            message = u"Waiting time exceeded."
        super(TimeOutException, self).__init__(message)


class NotFoundException(Exception):
    """Not found exception"""

    def __init__(self, message=None):
        if not message:
            message = u"Content not found."
        super(NotFoundException, self).__init__(message)


class BadRequestException(Exception):
    """Bad request exception"""

    def __init__(self, message=None):
        if not message:
            message = u"The request has invalid parameters."
        super(BadRequestException, self).__init__(message)
