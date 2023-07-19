from django.db import models

class Movie(models.Model):

    MY_CHOICES = (
        ('a', 'Sci-Fi'),
        ('b', 'Romance'), 
        ('c', 'Action'),
        ('d', 'Horror'),
        ('e', 'Thriller'),
        ('f', 'Comedy'),
    )

    title = models.CharField(max_length=355)

    category = models.CharField(max_length=1, choices=MY_CHOICES)
    