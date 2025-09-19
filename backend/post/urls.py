
from django.contrib import admin
from django.urls import include, path
from  post.views import *

urlpatterns = [
   #~post
    path("data/",data.as_view()),
    path("create/",UplodaPost.as_view()),
    path("update/<str:post_id>/",UpdatePost.as_view()),
    path("delete/<str:post_id>/",DeletePost.as_view()),
    
    #~ comment
    path("<str:post_id>/uploadcomment/",CommentCreate.as_view()), #? create comment
    path("<str:comment_id>/deletecomment/",deltedComment.as_view()), #? delete comment <str:comment_id>")
    path("<str:comment_id>/updatecomment/",UpdateComment.as_view()), #? delete comment <str:comment_id>")
    
    
#? like
path("<str:post_id>/like/",Likpost.as_view()),
]
