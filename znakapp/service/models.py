from django.conf import settings
from django.utils.timezone import now
from django.db import models


class UserInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return '{0} '.format(self.user)


class UserRequests(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    platform = models.CharField(max_length=20)
    addres = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=now, editable=False)
    lot_link = models.TextField()
    download_link = models.TextField()

    def __str__(self):
        return '{0} '.format(self.user)
