Fragrances Data Base

This project was build to facilitate the manage of a fragrance data-base where each fragrance has multiples descriptions to filter by.
The project was build in Django/Python and this app uses the django features to manage users and filters.
Each users can comment in each fragrance, and this comments can be used as a filter key words as well, this feature improve the time spenging in finding the right fragrance with the right description or cathegorie.

steps to download the app:

1. clone the repository 
  git clone https://github.com/andresnino1/fragrances.git

2. create and start a virtual environment
  pipenv shell
  
3. insall the project dependencies

 pip install -r requirements.txt
 
4. make django data-base migrations
 python manage.py makemigrations
 
5. migrate django data-base
 python manage.py migrate
 
6. run django server
 python manage.py runserver
 


