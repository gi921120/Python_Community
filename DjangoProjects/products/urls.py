from django.urls import path

from . import views # Report views from the current folder 

urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.new)
]