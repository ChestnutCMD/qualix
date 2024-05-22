from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h2)!8qps_5!ms4kfdhwy*wc6xiv#zu&1h**8ilhquvmlrt+wa0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jsonrpcapp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'testtask.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'testtask.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

CLIENT_CERT = """-----BEGIN CERTIFICATE-----
MIIDNjCCAh4CAwX1sjANBgkqhkiG9w0BAQsFADBpMQswCQYDVQQGEwJSVTEMMAoG
A1UECAwDVWZhMQwwCgYDVQQHDANVZmExDDAKBgNVBAoMA3NsYjEMMAoGA1UEAwwD
c2xiMSIwIAYJKoZIhvcNAQkBFhNzdXBwb3J0QHNsYi5tZWR2LnJ1MB4XDTI0MDQy
MjEwNDUzMFoXDTI1MDQyMjEwNDUzMFowVzELMAkGA1UEBhMCUlUxDzANBgNVBAgM
Bk1vc2NvdzEPMA0GA1UEBwwGTW9zY293MQ0wCwYDVQQKDARUZXN0MRcwFQYDVQQD
DA50ZXN0QHRlc3QudGVzdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
AI8n9wvUNCPFINPwQPeOHa33w/5j5Mg9UtgemAgj310JxL5yD1ec+ogNLn2uFkxi
oLFQIQHu2TPhsAc/G8QEQChDGK16g6O2DMjzRmXWbW6maq0B3FaPD8bQ4EL5hb6v
Rod3MnAAe+WfCm005mEyhT9gUY9pX8b0c+5IglFTITpf1Z/NDl98gnOIS8CznTid
Tor7pK9IPoJquXej0kHkgduzU2iQDcXHRRmQrKF28GFMgoZB+WMlr1cLSsTnp6r4
A06EgeBzbJ4JSzByEX++MAOg99yg5CjmePhvGklUC+4B6U0wUBXR9pIzasWByoQ/
ql8UGc79I0VQyWPEUV1w7ZECAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAA1Xm5oiJ
HAg/Dpu5f+dB+v5RRJhh0/DAD1eL1m4YtWUsOd+p7HaJXSjnybQ/Ok6Fashs4l79
Fep5sefmNvyMTpofwjdYe+1HTOuEoSwjLDe3gmV/qZN8Cc3EZVr8Gpg/UHNqT55B
oKu7M8DSwXjSPKxx+z4+l/B3cOu0zZZnaKUrbbyAwqKoXtfWqQKZmX5TlbZHwHhq
3KqdWquuRN77ok5B2UQASqTJQmgi6SVdqE8KVCnUv2SIMoSjhCBLLaKjfijeJE47
9nyLgg+fsMdQUPV74jA6SBlMCBSdsKjFXWVSlPbESRwd2m+6pCa0aGPm7lztdu+q
nv19azTWQJBa8Q==
-----END CERTIFICATE-----"""

CLIENT_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCPJ/cL1DQjxSDT
8ED3jh2t98P+Y+TIPVLYHpgII99dCcS+cg9XnPqIDS59rhZMYqCxUCEB7tkz4bAH
PxvEBEAoQxiteoOjtgzI80Zl1m1upmqtAdxWjw/G0OBC+YW+r0aHdzJwAHvlnwpt
NOZhMoU/YFGPaV/G9HPuSIJRUyE6X9WfzQ5ffIJziEvAs504nU6K+6SvSD6Carl3
o9JB5IHbs1NokA3Fx0UZkKyhdvBhTIKGQfljJa9XC0rE56eq+ANOhIHgc2yeCUsw
chF/vjADoPfcoOQo5nj4bxpJVAvuAelNMFAV0faSM2rFgcqEP6pfFBnO/SNFUMlj
xFFdcO2RAgMBAAECggEABkbA9L/Prrx3J/5MmuNG4dhkZhmIb6Rgpsu7QVVxTD71
ZUl9lWBzNivTHKeD9W1i5jiWeeM4RVILybA2o21xnVJJGVyvENUWfROiw9bsOAG2
g5ylRcDtTCY0RDt0ZbEsQnGIwJME25hmzfWXyYMm3GnN/vT7wgP4YTtvRemDIhqo
vgfJ92yhKhlLhbYL4ivcmsCajaBFN4PI/1RdubguCGTTbLKQaK4hjcsNWifut4cg
WUTPwzNwtyATYOq2JcCTKNEcWMrz9q9sMoXgUciOH1jG6b82B5yMUqjSvPVsz/AC
lNgVt1lyEJs3RSWy4iVOyQx5z+VhCsdmBcLGJxUoUQKBgQDF2dJz8jufCzi92beW
1OE2GcwWaUD0ut7cHMbMCs5iUKaTKrmgFW57mMfzRpUdTtE/ta/zWKbJlTQiereL
qsR937WTt2XUFtpwGMHgUVId/hUu/IFbs6b11IwFOJfbApGVLYr5372bqrectmAG
qdiPPIRBkZG6oHxAkSBxucUvGwKBgQC5OvF01t3/6ZOY63pHeBI2BsIH1pYP8jkF
HGAUDAg/F1Psp0SR/PrcKQ97eYkCCzCNBoSgeLA0SehHNNtBYSG9YR98x9LYLJko
Io0h4yXfL9DXBk3h5Uc9XDY7ZU0y78LI0k+yNTQvPjUiQFhJ3bZCIH1LrJBFHEwW
jxguHX7kwwKBgD6EzxiuUaK3JA3xzy6NREEZM8FdLxZmOmfpe/Qb8g1lGM3mMVPh
kdDifURlaFcjgcGVAu1tdP679AZ1KqyqoH56A2GTEU1Mj2femtzsNXuev0jip2m3
wilqKXi44ltlW2V9R64fwkV/U5fklUFlyDWy1MP3YMpNThYFBfCJ2EJDAoGBAKl8
E38zM8J7uP/NRv+qEA+7M0L0yC4jFqVkh00QjWMdNz9s9cMW1XspXu8+D2z9TBle
A3DJvYC6t3ygEpbKB5M/EQ6d0IDYnfMpWjXNn9ON7usw64ZswjiU7VJ/qJmY5IPY
W+/V2r/3jaqfcal04tWy4LKjXQa/k6d4m0lm17r9AoGBAJBXuJwK4ev76fZ1Y7rJ
lDAwjhme8t2dJ/aG12TNnschxAe/7LRwxRyMIu63ALhD5Air8VkdVCz+kb9P2Ny1
ZEyshP7wsIqb42cW94CzIyiLwLzT07jfu4GdNv5tekmdj5bzstreJPFIVRvfZwO/
Ar4XzwkZ3fClYyItc1jMoBIk
-----END PRIVATE KEY-----"""