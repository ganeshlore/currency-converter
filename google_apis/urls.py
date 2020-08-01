from django.urls import path
from . import views

app_name = 'google_apis'
urlpatterns = [
    path('convert_currency', views.convert_currency, name='convert_currency')
]