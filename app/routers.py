from rest_framework import routers
from app.views import CredentialView


class CredentialRouter:
    router = routers.SimpleRouter()
    router.register('login', CredentialView, basename='login')