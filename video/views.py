from django.shortcuts import render, redirect, get_object_or_404
from video.forms import CreatePostForm
from video.models import Post
from account.models import Account
from django.db.models import Q

def create_video_view(request):

    context={}

    user=request.user
    if not user.is_authenticated:
        return redirect('hitelesites_szukseges')
    
    if user.is_authenticated and not user.feltolto:
        return redirect('nincs_jogosultsag')
    
    form= CreatePostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj=form.save(commit=False)
        author=Account.objects.filter(email=user.email).first()
        obj.author=author
        form.save()
    context['form']=form

    return render(request, 'video/feltoltes.html',context)

def detail_video_view(request, slug):
	
	context = {}
	post = get_object_or_404(Post, slug=slug)
	context['post'] = post

	return render(request, 'video/detail_video.html', context)

def get_video_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = Post.objects.filter(
			Q(tancnev__contains=q)|
			Q(tanctipus__icontains=q)|
            Q(adatkozlo__icontains=q)|
            Q(talyegyseg__icontains=q)
			).distinct()
		for post in posts:
			queryset.append(post)

	return list(set(queryset)) 

