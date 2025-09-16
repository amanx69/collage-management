from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .Serializer import postSerializer
from rest_framework import status
from  rest_framework import  permissions




#! uploae  the 

class UplodaPost(APIView):  
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request):
        ser=postSerializer(data=request.data, context={"request": request})
        if  ser.is_valid():
            ser.save()
            return Response({
                "data":ser.data,
                "status":status.HTTP_201_CREATED,
                "message":"post created successfully"
                
            })
            
        else:
            return Response({
                "error":ser.errors,
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"post not created",
                "error":"error come for create post"
            })
        
        




class  data(APIView):
    def get(self, request):
        obj = Post.objects.all()
        ser = postSerializer(obj, many=True)
        return Response(ser.data)