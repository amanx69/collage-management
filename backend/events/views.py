from rest_framework.decorators import api_view
from rest_framework.response import Response
from events.Serializer import AnnouncementSerializer
from events.models import Announcement

@api_view(['GET', 'POST'])

def get(request):
     
     if request.method == 'GET':
        obj=  Announcement.objects.all()
        ser= AnnouncementSerializer(obj, many=True)
        return Response(ser.data)
    
     else:
         data = request.data
         ser = AnnouncementSerializer(data=data)
         if ser.is_valid():
             ser.save()
         return Response(ser.data)
    
