from django.db import models

# Create your models here.
class Country(models.Model):
	name = models.CharField(unique=True,
							max_length=50,
							)
	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class AdministrativeArea(models.Model):
	name = models.CharField(null=True,
							blank=True,
							max_length=50,
							)
	country = models.ForeignKey(Country,
								on_delete=models.CASCADE,
								)

	class Meta:
		ordering = ['name']

	def display_country(self):
		return self.country

	def __str__(self):
		return self.name

class Locality(models.Model):
	name = models.CharField(max_length=50)
	state = models.ForeignKey(AdministrativeArea,
							  on_delete=models.CASCADE,
							  )
	country = models.ForeignKey(Country,
								on_delete=models.CASCADE,
								)

	class Meta:
		ordering = ['name', 'state', 'country']

	def display_state(self):
		return self.state

	def display_country(self):
		return self.country

	def __str__(self):
		return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    place_id = models.CharField(max_length=256)
    longitude = models.FloatField()
    latitude = models.FloatField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(AdministrativeArea, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def display_country(self):
        return self.country

    def display_state(self):
        return self.state

    def display_city(self):
        return self.city

    def __str__(self):
        return self.name	