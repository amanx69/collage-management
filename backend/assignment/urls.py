from django.urls import include, path
from .views import uplodeAssignment,AssignmentList



urlpatterns = [
   path("upload/",AssignmentList.as_view()),
    
]
