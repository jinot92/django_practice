# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')

    def summary(self):
            return self.body[:100]
    def pub_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    def __str__(self):
        return self.title
