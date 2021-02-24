
import sys


# https://github.com/HXLStandard/libhxl-python/blob/master/hxl/__init__.py#L55
# class HXLmException(Exception):
#     """Base class for all HXL-related exceptions."""

#     def __init__(self, message, data={}):
#         """Create a new HXL exception.
#         Args:
#             message (str): error message for the exception
#             data (dict): properties associated with the exception (default {})
#         """
#         super(Exception, self).__init__(message)

#         self.message = message
#         """The human-readable error message."""

#         self.data = data
#         """Additional properties related to the error."""

#     def __str__(self):
#         return "<HXLException: " + str(self.message) + ">"

# https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python/53469898#53469898  #noqa

class HXLmException(Exception):
    """Generic HXLmException"""

    def __init__(self, message, payload=None):
        self.message = message
        self.payload = payload  # you could add more args

    def __str__(self):
        # __str__() obviously expects a string to be returned, so make sure not to send any other data types
        return str(self.message)


class HXLmPoliticException(Exception):
    """Non-generic Exception for issues related to politcs

    Implementers may decide to explicitly catch this type of exception by own
    implementations or raised by other libraries.
    """

    def __init__(self, message, payload=None):
        self.message = message
        self.payload = payload  # you could add more args

    def __str__(self):
        return str(self.message)


class HXLmCrimeException(Exception):
    """Exception about local/international crime

    Implementers may decide to explicitly catch this type of exception by own
    implementations or raised by other libraries instead of stop imediatelly
    the tools that implement it.
    """

    def __init__(self, message, payload=None):
        self.message = message
        self.payload = payload  # you could add more args

    def __str__(self):
        return str(self.message)
