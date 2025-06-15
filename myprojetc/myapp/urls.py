from django.urls import path
import . views
# path allows us to import multiple urls

url patterns = [
    path('', views.index, name='index')
]