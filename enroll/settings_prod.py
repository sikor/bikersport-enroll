from enroll.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
import dj_database_url


DATABASES = {
    'default': dj_database_url.config()
}