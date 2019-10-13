from setuptools import setup

setup(
    name='django-auth-backend',
    version='0.1.0',
    packages=['django_auth0_backend'],
    license='MIT License',
    install_requires=[
        'jose>=1.0.0',
        'requests>=2.22.0',
        'social-auth-core>=3.2.0',
    ],
    extra_requires=[
        'nameparser',
    ],
)
