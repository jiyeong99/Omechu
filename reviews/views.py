from django.shortcuts import render,redirect
from reviews.models import Review,Comment
from reviews.forms import CommentForm, ReviewForm
# Create your views here.

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews,
    }
    return render(request, 'reviews/index.html',context)

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("reviews:index")
    else:
        form = ReviewForm()

    context = {
        "form": form,
    }
    return render(request, "reviews/create.html", context)


def comment_create(request,detail_pk):
    review = Review.objects.get(pk=detail_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review=review
            comment.user = request.user
            comment.save()
            return redirect("reviews:detail", detail_pk) 
    else:
        comment_form=CommentForm()
    context={
        'comment_form':comment_form
    }
    return render(request,'reviews/comment.html',context)

def comment_delete(request,detail_pk,comment_pk):
    detail = Review.objects.get(pk =detail_pk)   # 몇번 글인지? ( 가게 )
    comment = Comment.objects.get(pk=comment_pk) # 어떤 댓글인지?(리뷰)
    if request.user == comment.user:
        comment.delete()
    return redirect('reviews:index')
    # return redirect('reviews:detail',detail_pk)

def detail(request,detail_pk):
    review = Review.objects.get(pk=detail_pk)

    comments = review.comment_set.all()

    context = {
        'review' : review,
        'comments':comments,
    }
    return render(request,'reviews/detail.html',context)

def update(request,detail_pk):
    review = Review.objects.get(pk=detail_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("reviews:detail", detail_pk)
    else:
        form = ReviewForm(instance=review)

    context = {
        "form": form,
    }
    return render(request, "reviews/create.html", context)


