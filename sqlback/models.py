# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length = 30)
    num = models.IntegerField(default = 0)
    chi = models.IntegerField(default = 0)
    mat = models.IntegerField(default = 0)
    eng = models.IntegerField(default = 0)
    phy = models.IntegerField(default = 0)
    che = models.IntegerField(default = 0)
    allscore = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.name