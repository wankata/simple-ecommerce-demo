"""
Django settings for the development environments of the ecommerce project.

All common settings reside in settings.base

If you need specific setting to be different in the different variables,
put it in the environment setting files with the relevant values.
"""
from .base import *  # noqa: F401, F403

DEBUG = True
ALLOWED_HOSTS = []
