from django.shortcuts import render, redirect
from main_app.models import User
from .models import PostedMessage, Comment


def wall(request):
    if not 'user_id' in request.session:
        request.session.flush()
        return redirect('/')
    this_user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': this_user,
        'msg_posts' : PostedMessage.objects.all().order_by("-created_at")
    }
    return render(request, 'wall.html', context)

def post_msg(request):
    if not 'user_id' in request.session:
        request.session.flush()
        return redirect('/')
    this_user = User.objects.get(id=request.session['user_id'])
    PostedMessage.objects.create(
        content = request.POST['message'],
        user = this_user
    )
    return redirect('/wall')

def delete(request, post_id):
    if not 'user_id' in request.session:
        request.session.flush()
        return redirect('/')
    this_post = PostedMessage.objects.get(id=post_id)
    this_post.delete()
    return redirect('/wall')

def comments(request, post_id):
    if not 'user_id' in request.session:
        request.session.flush()
        return redirect('/')
    this_user = User.objects.get(id=request.session['user_id'])
    this_post = PostedMessage.objects.get(id=post_id)
    context = {
        'user': this_user,
        'msg': this_post,
        'comments': this_post.comments.all().order_by("created_at")
    }
    return render(request, 'comments.html', context)

def post_comment(request, post_id):
    if not 'user_id' in request.session:
        request.session.flush()
        return redirect('/')
    this_user = User.objects.get(id=request.session['user_id'])
    this_post = PostedMessage.objects.get(id=post_id)
    Comment.objects.create(
        content = request.POST['comment'],
        user = this_user,
        postedmessage = this_post
    )
    return redirect(f'/wall/{post_id}/comments')

def delete_comment(request, post_id, comment_id):
    if not 'user_id' in request.session:
        request.session.flush()
        return redirect('/')
    this_comment = Comment.objects.get(id=comment_id)
    this_comment.delete()
    return redirect(f'/wall/{post_id}/comments')

