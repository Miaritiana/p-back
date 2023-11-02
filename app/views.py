from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.serializers import CredentialSerializers
from app.models import Credentials


class CredentialView(ModelViewSet):

    queryset = Credentials.objects.all()
    serializer_class = CredentialSerializers