from django.db import models

class Visitor(models.Model):
    UID = models.CharField(blank=False, max_length=10)
    Name = models.CharField(blank=False, max_length=250)
    Points = models.IntegerField(blank=False)

    def __str__(self):
        return self.Name