
from django.contrib import admin
from django.urls import include, path
from  post.views import *

urlpatterns = [
   #~post
    path("data/",data.as_view()),
    path("create/",UplodaPost.as_view()),
    
    
    #~ comment
    path("<str:post_id>/uploadcomment/",CommentCreate.as_view()), #? create comment
    path("<str:comment_id>/deletecomment/",deltedComment.as_view()), #? delete comment <str:comment_id>")
    
#? like
path("<str:post_id>/like/",Likpost.as_view()),
]
