from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    years_of_life = models.CharField(max_length=50, blank=True, null=True)  # позволяет пустые значения
    biography = models.TextField(blank=True) # позволяет пустые значения
    image1 = models.ImageField(blank=True, upload_to='static/assets/images')
    image2 = models.ImageField(blank=True, upload_to='static/assets/images')
    image3 = models.ImageField(blank=True, upload_to='static/assets/images')
    image4 = models.ImageField(blank=True, upload_to='static/assets/images')
    image5 = models.ImageField(blank=True, upload_to='static/assets/images')


    def __str__(self):
        return self.full_name
