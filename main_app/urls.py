from . import views
from django.urls import path

app_name = 'main_app'
urlpatterns = [
    path('', views.index, name='index'),
]