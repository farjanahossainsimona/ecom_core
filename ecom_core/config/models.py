from django.db import models

class DateModel(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    
    class Meta:
        abstract = True

