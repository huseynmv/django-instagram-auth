
from django.urls import path, include
from .views import home, login, register, add_instagram
app_name='account'
urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('add-instagram/', add_instagram, name='add-instagram'),


]