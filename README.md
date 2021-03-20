# django-location-app
A Django app that helps you easily create and manage your own location data. Simply get a [google maps api key](https://developers.google.com/maps/gmp-get-started) and configure your maps directly from your django project's settings. Map comes with autocomplete functionality and saves your location to a completely normalized location database. See below for [ORM diagram](https://github.com/AnmolChachra/django-location-app#ORM)

## Quickstart
Install django-location-app available on [pypy](https://pypi.org/project/django-location-app/1.0.0) and add it to your INSTALLED_APPS in your project's settings.py file<br>
```
pip install django-location-app

INSTALLED_APPS = (...
                  'location_app',
                  ...
                 )
```
Get your Google MAPS API key from [here](https://developers.google.com/maps/gmp-get-started) and add it to the settings. It is always a good idea to store the key as an environment variable and access via ```os.environ.get(<name>)```. [Learn more](https://dev.to/biplov/handling-passwords-and-secret-keys-using-environment-variables-2ei0)
```
LOC_APP_MAPS_API_KEY = XXXXXXXXXXXXXXXXXXXXXX
```
To see if installation was successful, add the following to your project's urls.py file
```
from django.urls import path, include
urlpatterns += [path('location/', include("location_app.urls")),]
```
If in dev, visit http://localhost:[Port]/location/ and you should see the following UI

https://user-images.githubusercontent.com/22666819/111712391-ead51c80-8823-11eb-96a3-9eb55f3cbe4c.mp4

## ORM
![image](https://user-images.githubusercontent.com/22666819/111717494-879cb780-882e-11eb-9034-e717785961da.png)
