from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post 

def home(request):
    # Posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-date') 
    return render(request, 'main.html', {'posts':posts})

def postcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')    
    else: 
        form = PostForm()
    return render(request, 'post_form.html',{'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail})

#댓글 저장
def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filed_form.save(commit=False)
        finished_form.post = get_object_or_404(post, pk=post_id)
        finished_form.save()

    return redirect('detail', post_id)



# 공동구매&배달음식 페이지
def coBuying(request):
    return render(request,'coBuying.html')

def delivery(request):
    return render(request,'delivery.html')

def detailView(request):
    return render(request,'detailView.html')