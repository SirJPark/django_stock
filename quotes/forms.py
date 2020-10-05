from django import forms 

# import the models as we need this to connect to our models. Import the Stock class
from .models import Stock 

class StockForm(forms.ModelForm):
	class Meta: 
		model = Stock 
		fields = ["ticker"]
