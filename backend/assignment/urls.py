from django.urls import include, path
from .views import uplodeAssignment



urlpatterns = [
   path("upload/",uplodeAssignment.as_view()),
    
]
