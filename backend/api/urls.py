
# from django.contrib import admin
# from django.urls import include, path  
# from django.conf import settings
# from django.conf.urls.static import static
# from events import views as event
# from users import views as user

# #! for auth token
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )





# urlpatterns = [
#      #! for auth token
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    
#     path("admin/", admin.site.urls),
#     path("event/", event.get,),
#     path("login/",user.login.as_view()), #! LOGIN
#     path("singup/", user.SingUp.as_view()), #! SINGUP
#     path("logout",user.Logout.as_view()), #!@ LOGOUT
#     path("data/", user.data.as_view()),
#     path("addname/",user.UpdateName.as_view()),

    
  
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)