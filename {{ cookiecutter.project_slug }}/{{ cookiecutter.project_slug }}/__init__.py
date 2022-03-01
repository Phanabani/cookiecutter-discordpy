import logging
logger = logging.getLogger(__name__)

from .{{ cookiecutter.project_slug }} import *

__version__ = '{{ cookiecutter.version }}'
