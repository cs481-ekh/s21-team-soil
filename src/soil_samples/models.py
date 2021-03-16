from django.db import models

class soil_sample(models.Model):
    lime_or_cement_stabilization = models.CharField("Name", max_length=240)
    dose_of_lime_or_cement = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
