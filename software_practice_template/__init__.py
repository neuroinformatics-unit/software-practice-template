from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("software-practice-template")
except PackageNotFoundError:
    # package is not installed
    pass
