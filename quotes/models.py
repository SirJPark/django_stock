from django.db import models

#create a class called Stock and parse in models.Model
class Stock(models.Model):
	ticker = models.CharField(max_length=10)

	#this is for admin area 
	def __str__(self):
		return self.ticker 
