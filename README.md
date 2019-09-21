# django-auth0-backend
An Auth0 authentication backed for Django.

## Installation

1. Install django-auth0-backend
  ```
  pip install django-auth0-backend
  ```

2. Add `django_auth0_backend` to your installed apps.
```
INSTALLED_APPS = [
...
'django_auth0_backend',
...
]
```

3. Add `django_auth0_backend.auth0_backend.Auth0Backend` to `AUTHENTICATION_BACKENDS`

```
AUTHENTICATION_BACKENDS = [
  ...
  'django_auth0_backend.auth0_backend.Auth0Backend',
  ...
]
  ```
4. Add the follow to settings.py
```
SOCIAL_AUTH_AUTH0_DOMAIN  = "custom.auth0.com"
SOCIAL_AUTH_AUTH0_KEY     = "XXXXXXXXXXXXXXXX"
SOCIAL_AUTH_AUTH0_SECRET  = "XXXXXXXXXXXXXXXX"
SOCIAL_AUTH_AUTH0_SCOPE = [
  'openid',
  'profile',
  'email',
]
LOGIN_URL = '/login/auth0'
```
