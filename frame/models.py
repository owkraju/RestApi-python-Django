# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Data(models.Model):
	name=models.CharField(max_length=20)
	did=models.IntegerField()
	
	def __str__(self):
		return self.name
