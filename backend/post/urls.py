
from django.contrib import admin
from django.urls import include, path
from  post.views import data

urlpatterns = [

    path("data/",data.as_view()),

]
