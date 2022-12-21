from django.shortcuts import render

def post(request):
    posts = Post.object.all()
    context = {
      'posts' : posts
    }
return render(request , 'index.html' , context ,)