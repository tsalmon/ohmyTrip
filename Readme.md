# HoMyTrip

## Introduction

Know your futur travel.

## Secrets settings 

To make this application runnable, you have to add a file named `secret_settings.py` into the `hometrip/` folder, which allow you to communicate with Api used by the application (at this point(6/03/2015), we use facebook connect, google place and yelp api).

Paste the following code into this file, and go to links specified to see what to do.

```python
import os 

# GENERALS SETTINGS
#-----------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = # see: http://www.miniwebtool.com/django-secret-keygenerator/

DATABASES = { # see: https://docs.djangoproject.com/en/1.7/ref/databases/
    'default': {
        'ENGINE': ,
        'NAME': ,
    }
}

# FACEBOOK LOGINS SETTINGS (see: https://developers.facebook.com/ and make a new app)
#-----------------------------------------------------------
from authomatic.providers import oauth2#, oauth1, gaeopenid

AUTHOMATIC_CONFIG = {
    'fb': {
        'class_': ,
        # Facebook is an AuthorizationProvider too.
        'consumer_key': '',
        'consumer_secret': '',
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ,
    }
}

# YELP SETTINGS (see: https://www.yelp.com/developers/manage_api_keys)
#-----------------------------------------------------------
YELP_CONSUMER_KEY = ''
YELP_CONSUMER_SECRET = ''
YELP_TOKEN = ''
YELP_TOKEN_SECRET = ''
```