from django.db import models
from django.contrib.auth.models import User
from .utils import sendTransaction
import hashlib
from datetime import datetime

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.now, blank=True)
    content = models.TextField()
    hash = models.CharField(max_length=32, default=None, null=True)
    txId = models.CharField(max_length=66, default=None, null=True)

    def writeOnChain(self):
        self.hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
        #self.save()

class UserIpLog(models.Model):
    user = models.TextField()
    ip = models.TextField()
