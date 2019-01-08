"""
Django settings for the production environment of the ecommerce project.

All common settings reside in settings.base

If you need specific setting to be different in the different variables, 
put it in the environment setting files with the relevant values.
"""
from .base import *

DEBUG = False
# Change this, when production host name is known
ALLOWED_HOSTS = ['*']

