from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import assigment
from .Serializer import AssignmentSerializer
from rest_framework import generics
from post.models import Post
from post.Serializer import postSerializer
from rest_framework import permissions
class uplodeAssignment(APIView):
    
  

    def post(self, request):
        data = request.data
        if not isinstance(data, list):
            data = [data]
        ser = AssignmentSerializer(data=data, many=True)

        if ser.is_valid():
            ser.save()
            return Response(
                {
                    "data": ser.data,
                    "message": "success",
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {
                    "error": ser.errors,
                    "status": status.HTTP_400_BAD_REQUEST,
                    "error_source": "error occurred while uploading assignment",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        
 

class AssignmentList(APIView):
    permission_classes=[permissions.IsAuthenticated]
   
 
    def get(self, request):
        user = request.user  # Current authenticated user
        return Response({
            "username": user.full_name,
            
        })
    
    
    
   