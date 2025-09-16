from django.urls import include, path
from faculty.views import uploadunnouncement ,updateAnnouncement,deleteAnnouncement




urlpatterns = [
    #! for announcement
    path("upload/",uploadunnouncement.as_view()),
    path("<str:pk>/update/",updateAnnouncement.as_view()),
    path("<str:pk>/delete/",deleteAnnouncement.as_view()),
    
  
    
]
