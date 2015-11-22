from django.db import models

'''
class yum (models.Model):
    pic_url = models.CharField(max_length = 50)
    translation = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
'''

class Word(models.Model):
    pic_url = models.CharField(max_length = 50)
    translation = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
