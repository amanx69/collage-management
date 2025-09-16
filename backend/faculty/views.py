from rest_framework.response import Response
from rest_framework.views import APIView
from events.models import Announcement
from events.Serializer import AnnouncementSerializer
from rest_framework import status  
from rest_framework import permissions
from  events.models import Announcement
from .permissions import isFaculty





#!  save  announcement 

class uploadunnouncement(APIView):
   permission_classes=[isFaculty|permissions.IsAdminUser]

 #~  save  announcement in data base 
   def post(self, request):
        user= request.user #!  current user 

      #! if data is dic convert it to list
        data= request.data
        if not isinstance(data, list):
              data=[data]
              ser= AnnouncementSerializer(data=data,many=True)
        if ser.is_valid():
              ser.save(user=user)
              return Response(
                  {
                      "data":ser.data,
                      "status":status.HTTP_201_CREATED,
                      "message":"announcement created successfully"
                  }
              )
        else:
              return Response(
                  {
                      "error":ser.errors,
                      "status":status.HTTP_400_BAD_REQUEST,
                      "message":"announcement not created"
                  }
              )
              
#! upldate  announcement

class  updateAnnouncement(APIView):
   permission_classes=[isFaculty|permissions.IsAdminUser]
   
   def  patch(self,request,pk):
       
    try:
       annoumnet= Announcement.objects.get(pk=pk)
        
    except Announcement.DoesNotExist:
        return Response({
            "error":"Announcement not found",
            "status":status.HTTP_404_NOT_FOUND,
            
        })
        
        #! if  user  is  faculty than save announcement
  
    if request.user.role=="faculty": 
             
        ser= AnnouncementSerializer(annoumnet,data=request.data,partial=True)
        if ser.is_valid():
                ser.save()
                return  Response({
                    "data":ser.data,
                    "status":status.HTTP_200_OK,
                    "message":"announcement updated successfully"
                })
        else:
                return Response({
                    "error":ser.errors,
                    "status":status.HTTP_400_BAD_REQUEST,
                    "message":"announcement not updated",
                    "error sourse":" error come for update announcement"
                    
                })
                
                
                
            
            
#! delerte  announcement

class deleteAnnouncement(APIView):
    permission_classes=[isFaculty|permissions.IsAdminUser]
    
    def delete(self,request,pk):
        try:
            annoumnet=Announcement.objects.get(pk=pk)
            annoumnet.delete()
            return Response({
                "deleted id":annoumnet.pk,
                "status":status.HTTP_200_OK,
                "message":"announcement deleted successfully"
            })
            
        except Announcement.DoesNotExist:   
            return Response({
                "error":"Announcement not found",
                "status":status.HTTP_404_NOT_FOUND,
                
            })