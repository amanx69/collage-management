from  rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from faculty.permissions import isFaculty
from rest_framework import permissions
from .models import assigment
from .Serializer import AssignmentSerializer





class  uplodeAssignment(APIView):
    
    def get(self, request):
        
        obj= assigment.objects.all()
        ser=AssignmentSerializer(obj,many=True)
        return Response(ser.data)
    

        