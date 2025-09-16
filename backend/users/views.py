from rest_framework.response import Response
from .Serializer import UserSerializer, NameSerializer, BioSerializer
from rest_framework.views import APIView 
from .models import User
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate #! import  for  auth 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed

#! see  the  view set used  for  crud operation like  get ,post ,update ,delete single  item

#? functrion for  gernate  token
def get_token(user):
    if not user.is_active:
      raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    } 





 #! class  for sing  up 
class SingUp(APIView):
	permission_classes = [AllowAny]

	def post(self, request):
		
	
		data = request.data
		serializer = UserSerializer(data=data)
		if serializer.is_valid():
			user =serializer.save()
			token=get_token(user)
            
			return Response(
				{
					"massage":"User Created Successfully",
                    "data":serializer.data,
                    "status=":status.HTTP_201_CREATED,
                    "token":token,
                    "email":request.data.get("email"),
				}
              
			 )
                
		else:

			return Response({
				"error":serializer.errors,
				"status":status.HTTP_400_BAD_REQUEST,
                "massage":"User Not Created enter  requirled field "
    
    
			})
      
			
    

#! class  for  login
class login(APIView):
	permission_classes = [AllowAny]
     
	def post(self, request):
     
     
		"""
		Handles login request and returns a JSON Web Token (JWT) if
		credentials are valid.

		Args:
			request (Request): The request object.

		Returns:
			Response: A response object containing the access token and
			refresh token, or a 400 response if credentials are invalid, or
			a 401 response if the user is inactive or if the credentials
			are invalid.
		"""
     
		email = request.data.get("email")
		password = request.data.get("password")
       
        #! if  user  not enter email or password  return  error

		if not email or not password:
			return Response({
                 "error": "Email and password are required.",
                 "status": status.HTTP_400_BAD_REQUEST
                 
       
                    }, status=status.HTTP_400_BAD_REQUEST)
   
       
   #! if  email not found  data base 
		elif not User.objects.filter(email=email).exists():
			return Response({
				"error": "email not found.",
				"status": status.HTTP_404_NOT_FOUND
			}, status=status.HTTP_404_NOT_FOUND)
        
   

		user = authenticate(request=request, username=email, password=password)
		if user is None:
			return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)  #!  if user  dont exist  return  error message	

		refresh = RefreshToken.for_user(user)
		return Response(
			{
				"access": str(refresh.access_token),
				"refresh": str(refresh),
				"user": {
					"id": user.id,
					"email": user.email,
				}
			},
			status=status.HTTP_200_OK
		)




#! log out  funcllaty
class Logout(APIView):
    parser_classes=[IsAuthenticated]
    
    
    def post(self, request):
					
					try:
					
						refresh_token= request.data["logout"]
						token=RefreshToken(refresh_token)
						token.blacklist()
						return Response({"massage":"logout"},status=status.HTTP_200_OK)
				
					except Exception as e:
						return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    
    
    
#! class  fro update  usenname and  date of  birth 

class UpdateName(APIView):
 permission_classes = [IsAuthenticated]
    
 def patch(self, request, pk):
     
    user=request.user

    try:
        User.objects.get(pk=pk)  #  for get  user if  not  give  error
   
            
    except User.DoesNotExist:
        return Response({
            "error": "User not found",
            "error sourse": "error  come for add name and  dof"
            
            }, status=status.HTTP_404_NOT_FOUND)

    serializer = NameSerializer(instance=user, data=request.data, partial=True)  


    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({
            "data": serializer.data,
            "status": status.HTTP_200_OK,
            "message": "User updated successfully"
        })
    else:
        return Response({
            "error": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "User not updated"
        })	



#!  class  for  update  bio and  profile  image 

class updateBioPfroile(APIView):
 permission_classes = [IsAuthenticated]
    
    
 def patch(self, request, pk):
     
     user=request.user
     try:
             User.objects.get(pk=pk)
         
     except User.DoesNotExist:
         return Response({
             "error":"User not found",
              "error sourse": "error  come for add bio and  profile  "
                          },status=status.HTTP_404_NOT_FOUND)
         
     ser=BioSerializer(instance=user,data=request.data,partial=True)
     
     if ser.is_valid():
         ser.save()
         return Response({
             "data":ser.data,
             "stus":status.HTTP_200_OK,
			 "message":"User updated successfully"
			 
    
		 })
         
     else:
         return Response({
			 "error":ser.errors,
			 "status":status.HTTP_400_BAD_REQUEST,
			 "message":"User not updated"
    
		 })   
         


class data(APIView):
    permission_classes=[AllowAny]
    
    def get(self, request,pk):
        users =  User.objects.get(pk =pk)
        serializer = UserSerializer(users,)
        return Response(serializer.data)
  
  

  
class alldata(APIView):
    permission_classes=[AllowAny]
    
    def get(self, request,):
        
        return Response({
            "name":request.user.full_name,
            "email":request.user.email,
            "role":request.user.role,
			"id":request.user.id,
			
			"bio":request.user.bio,
			"dateofbirth":request.user.dateofbirth
			
			
		})

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
