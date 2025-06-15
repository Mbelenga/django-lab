from django.urls import path
from . import views
# path allows us to import multiple urls

urlpatterns = [
    path('', views.index, name='index')
]