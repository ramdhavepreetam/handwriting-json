"""Handwriting JSON public API."""

from .extract import extract
from .models import DocumentInput, ExtractionResult

__all__ = ["DocumentInput", "ExtractionResult", "extract"]

__version__ = "0.1.0"
