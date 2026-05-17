"""Typed errors raised by Handwriting JSON."""


class HandwritingJsonError(Exception):
    """Base class for package errors."""


class InputError(HandwritingJsonError):
    """Raised when an input document cannot be normalized."""


class ProviderError(HandwritingJsonError):
    """Raised when an LLM provider request fails."""


class ResponseParseError(HandwritingJsonError):
    """Raised when provider output cannot be parsed as JSON."""


class SchemaError(HandwritingJsonError):
    """Raised when schema guidance is invalid."""
