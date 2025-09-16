
from django.contrib import admin
from django.urls import include, path
from  post.views import *

urlpatterns = [

    path("data/",data.as_view()),
    path("create/",UplodaPost.as_view()),

]
