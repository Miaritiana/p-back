from rest_framework.serializers import ModelSerializer
from app.models import Credentials


class CredentialSerializers(ModelSerializer):

    class Meta:
        model = Credentials
        fields = ["cliId","username","password"]