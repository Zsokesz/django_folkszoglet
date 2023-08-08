from django.shortcuts import render
from django.http import HttpResponse
from video.models import Post
from video.views import get_video_queryset
from operator import attrgetter

def fooldal(request):
    return render (request, 'index.html')
def about(request):
    return render (request, 'about.html')
def prtfolio(request):

    context={}

    query = ""
    if request.GET:
        query = request.GET.get('q',"")
        context['query'] = str(query)
        context['filter'] = request.GET.get('filter',"")


    posts=sorted(Post.objects.all(), key=attrgetter('tancnev'), reverse=True)
    blog_posts = sorted(get_video_queryset(query), key=attrgetter('tancnev'), reverse=True)
    context["posts"] = blog_posts
    return render (request, 'portfolio.html', context)