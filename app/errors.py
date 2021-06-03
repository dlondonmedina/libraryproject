class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ItemUnvailableError(Error):
    """Exception raised for errors if object is unavailable"""
    pass

class CannotCheckInError(Error):
    pass