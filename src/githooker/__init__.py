from importlib.metadata import PackageNotFoundError, version

from .githooker import PreCommit

__title__ = "githooker"

try:
    __version__ = version(__title__)
except PackageNotFoundError:
    __version__ = "0.0.0"

__author__ = "Kamil Cyganowski"
__license__ = "MIT"
__copyright__ = "Copyright 2026 Kamil Cyganowski"
__all__ = ["PreCommit"]
