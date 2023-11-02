from django.db import models


class Credentials(models.Model):
    cliId = models.CharField()
    username = models.CharField()
    password = models.CharField()