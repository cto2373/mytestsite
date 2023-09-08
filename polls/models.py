from django.db import models
from rest_framework.reverse import reverse


# Create your models here.
from django.db import models
class Genre(models.Model):
    
    name = models.CharField( max_length=240)
    
    def __str__(self):
        return self.name

    
    
class Actor(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('actor-detail', args=[str(self.id)])

class Movie(models.Model):
    MPA = [
        ("G", "General Audiences"),
        ("PG", "Parental Guidance Suggested"),
        ("PG-13", "Parents Strongly Cautioned"),
        ("R", "Restricted"),
        ("NC-17", "Adults Only"),
        ("NR", "Not Rated"),
    ]
    title = models.CharField("Title", max_length=240)
    starRating = models.DecimalField(max_digits=4, decimal_places=2)
    rating = models.CharField("Rating", choices=MPA, max_length=5, default='NR')
    year = models.DateField("Years", auto_now=False, auto_now_add=False)
    genre = models.ForeignKey(Genre ,on_delete=models.SET_NULL, null=True)
    runTime = models.DecimalField(max_digits=4, decimal_places=2)
    cast = models.ManyToManyField(Actor, help_text="")
    iamge = models.CharField("Image", blank=True, max_length=512)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self, request=None, format=None):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('movie-detail', args=[str(self.id)], request=request, format=format)