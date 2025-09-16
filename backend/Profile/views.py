from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import  User
from .Serializer import  ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes



#! i option  the show  the  profile
class ShowTheProfile(APIView):
    
    def get(self, request,pk):
        obj= User.objects.get(id=pk)
        ser= ProfileSerializer(obj)
        return Response(ser.data)
    
class Showprofile(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self, request):
        obj= request.user
        ser= ProfileSerializer(obj)
        return Response(ser.data)
  
    
    