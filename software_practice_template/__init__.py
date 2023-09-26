from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("rse-best-practices-playground")
except PackageNotFoundError:
    # package is not installed
    pass
