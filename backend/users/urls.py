
from django.contrib import admin
from django.urls import include, path  
from django.conf import settings
from django.conf.urls.static import static
from users import views as userview

#! for auth token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)





urlpatterns = [
     #! for auth token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  

    path("login/",userview.login.as_view()), #! LOGIN
    path("singup/", userview.SingUp.as_view()), #! SINGUP
    path("logout",userview.Logout.as_view()), #!@ LOGOUT
    path("data/", userview.alldata.as_view()),
    path("<str:pk>/", userview.data.as_view()),
    path("<str:pk>/addname/",userview.UpdateName.as_view()),
    path("<str:pk>/addbio/",userview.updateBioPfroile.as_view()),

    
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)