"Portfolio tracker" written following walkthrough lesson from Udemy course Top Web Development Bundle: Django, Ruby on Rails, Node.

It can search a financial tracking API if given an official ticker, and will return a small selection of information about that stock. 
There is a page with a table that you can add stocks to, this also returns a small selection of information from the API.
There is another page with a list of stocks that have been added to the database and can be removed. 
A Django messaging method has been added to display when a stock has been added or deleted.

Known issue: the close (cross) button doesn't work for messages

Room for improvement: There is a loop which calls the API for each stock, it would be better if it only called the API once for all the stocks in the table.

Portfolio tracker is written in HTML, Django, and Python. 

Requirements to run VE on Windows 

1. Install Sublime Text or other text editor	https://www.sublimetext.com/download_thanks?target=win-x64
2. Install gitbash	https://git-scm.com/download/win
3. Install Python	https://www.python.org/downloads/
4. In gitbash terminal run "mkdir /c/djangostock", "cd /c/djangostock", "pip install virtualenv", "python -m venv venv", "source venv/Scripts/activate", "pip install django", "django-admin startproject stocks"
5. Copy all folders and files from django_stock repo to /c/djangostock/stocks directory
6. In gitbash terminal run "python manage.py runserver"
7. Start a web browser and navigate to localhost:8000
8. After you're finished exploring, in gitbash terminal press CTRL + C to stop the server