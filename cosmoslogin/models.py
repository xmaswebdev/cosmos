# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class userLoginInfo(models.Model):
    user_id = models.CharField(max_length=25)
    user_access = models.CharField(max_length=25)
    user_password = models.CharField(max_length=200)
    user_name = models.CharField(max_length=40)
