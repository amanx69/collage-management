from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post,comments,Likes
from .Serializer import postSerializer,commentSerializer
from rest_framework import status
from  rest_framework import  permissions
from django.shortcuts import get_object_or_404




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
            
#! update  the post 

class UpdatePost(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def patch(self,request,post_id):
        
        
        post=get_object_or_404(Post,pk=post_id)
        #! if the user  is not the owner of the post
        if post.user != request.user:
            return Response({
                "status":status.HTTP_403_FORBIDDEN,
                "error":"You don't have permission to update this post",
              
            })
        ser= postSerializer(post,data=request.data,partial=True)
        if  ser.is_valid():
            ser.save()
            return Response({
                "data":ser.data,
                "status":status.HTTP_200_OK,
                "message":"post updated successfully",
           
            
               
                
            })
            
            
        else:
            return Response({
                "error":ser.errors,
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"post not updated",
        })    
            
            
#! delete the post 
class DeletePost(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def delete(self,request,post_id):
        post =get_object_or_404(Post,pk= post_id)    
        if post.user != request.user:
            return Response({
                "status":status.HTTP_400_BAD_REQUEST,
                "error":"You don't have permission to delete this post",
                "error":"you can delete only your post"
            })
            
        de= post.delete()   
            
        if  de:
            return Response({
                "status":status.HTTP_200_OK,
                "message":"post deleted successfully"
            })    
            
            
        else:
            return Response({
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"post not deleted",
                "error":"error come for delete post"
            })    
            
         
           
     
                
            
            #! create a comment 
class  CommentCreate(APIView):
    permission_classes= [permissions.IsAuthenticated]
    def post(self,request,post_id):
        
        try:
            post=Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({
                "status":status.HTTP_404_NOT_FOUND,
                "error":"post not found  "
        })   
            
        ser=  commentSerializer(data=request.data,context={"request": request,"post":post})  
        if ser.is_valid():
            ser.save(comment_user=request.user,post=post)    
            return Response({
                "data":ser.data,
                "status":status.HTTP_201_CREATED,
                "message":"comment created successfully"
            })
        else:
            return Response({
                "error":ser.errors,
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"comment not created",
            })
            
           #! fro  deleted the  comment 
class  deltedComment(APIView): 
    permission_classes=[permissions.IsAuthenticated]   
    def delete(self,request,comment_id):
        comment = get_object_or_404(comments, pk=comment_id)
        if comment.comment_user != request.user:
            return Response({
                "status":status.HTTP_403_FORBIDDEN,
                "message":"You deleted only your comment"
            })
        comment.delete()
        return Response({
            "status":status.HTTP_200_OK,
            "message":"comment deleted successfully"
        })  
        
        
#! update  the comment 
class UpdateComment(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def patch(self,request,comment_id):
        comment=get_object_or_404(comments,pk=comment_id)
        if comment.comment_user!= request.user:
            return Response({
                "status":status.HTTP_403_FORBIDDEN,
                "error":"You don't have permission to update this comment",
                "error":"you can update only your comment"
            })
        ser= commentSerializer(comment,data=request.data,partial=True)
        if  ser.is_valid():
            ser.save()
            return  Response({
                "data":ser.data,
                "status":status.HTTP_200_OK,
                "message":"comment updated successfully"
            })
        else:
            return Response({
                "error":ser.errors,
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"comment not updated"
            })    
        
        
        
        
#!  like the post 

class Likpost(APIView):
    permission_classes=[permissions.IsAuthenticated]
    
    def post(self,request,post_id):
        like_post=get_object_or_404(Post,pk=post_id)
        user= request.user
        
        like= Likes.objects.filter(user=user,post= like_post).first()
        if like:
            like.delete()
            return Response({
                "masage":"remove  like sussifully ",
                "stutes":status.HTTP_200_OK,
                "name":user.full_name
            })
        else:
            Likes.objects.create(user=user,post=like_post)
            return Response({
                "message":"like sussifully ",
                "stutes":status.HTTP_200_OK
                
            })
   
            
            
            
        




class  data(APIView):
    def get(self,request,):
        obj= Post.objects.all()
        ser=postSerializer(obj,many=True)
        return Response(ser.data)  