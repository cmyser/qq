import requests as r
from django.shortcuts import render
from .models import *




def index(request):

    
    
    

    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(body__icontains=search_query)
    else:
        posts = Post.objects.all()
        
    
    users = User.objects.all()
    posts = Post.objects.all()
    
          
 
    data = { "user": users, 'post': posts}
    return render(request, "show.html", context=data)



    

