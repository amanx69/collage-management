from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .Serializer import postSerializer


class  data(APIView):
    def get(self, request):
        obj = Post.objects.all()
        ser = postSerializer(obj, many=True)
        return Response(ser.data)