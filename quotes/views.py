#Walkthrough lesson completed from Udemy course Top Web Development Bundle: Django, Ruby on Rails, Node.

from django.shortcuts import render, redirect
from .models import Stock
from .forms	import StockForm
from django.contrib import messages

def home(request):
	import requests 
	import json 

	if request.method == 'POST':
		ticker = request.POST['ticker']
		# pk_ff9a4bfd2af54472aff9360f5a1138b0
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_ff9a4bfd2af54472aff9360f5a1138b0")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api': api})

	else:
		return render(request, 'home.html', {'ticker': "Enter a ticker symbol above."})




def about(request):
	return render(request, 'about.html', {})

def add_stock(request):
	import requests 
	import json 

	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added."))
			return redirect('add_stock')

	else: 
		ticker = Stock.objects.all()
		output = []
		for ticker_item in ticker:

			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_ff9a4bfd2af54472aff9360f5a1138b0")
			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."

		return	render(request, 'add_stock.html', {'ticker' : ticker, 'output': output})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Ticker deleted."))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker': ticker})