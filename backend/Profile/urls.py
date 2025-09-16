from django.urls import path 
from .views import *

urlpatterns = [
    path("show/",Showprofile.as_view()),
]
