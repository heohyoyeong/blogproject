from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Datt
from posts.forms import PostForm, DattForm

def p_list(request):
    my_list= Post.objects.all().order_by("-id")
    context={'posts':my_list}
    return render(request,'list.html',context)

def p_create(request):
    # POST 방식으로 호출될때 =>form action method="post"인 방식
    if request.method == 'POST':
        post_form=PostForm(request.POST) # POST방식으로 전송된것을 싹다 사용해서 객체로 만들어라!

        if post_form.is_valid(): # 제대로 된 값을 입력하였다면
            post_form.save()
            return redirect("posts:list") #다시 돌아간다!

    # GET 방식으로 호출될때 => form action을 사용하지않는 거의 모든 방식
    else:
        post_form=PostForm() #PostForm의 인자가 ()처럼 비어있기 때문에 비어있는 형태로 출력된다.

    return render(request, 'create.html',{'post_form':post_form})

def p_delete(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('posts:list')


def p_update(request,post_id):
    post= get_object_or_404(Post,pk=post_id)

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)

        if post_form.is_valid():
            post_form.save()
            return redirect("posts:list")

    else:
        post_form = PostForm(instance=post)

    return render(request, 'create.html', {'post_form': post_form})

def p_datt(request,post_id):
    post= get_object_or_404(Post,pk=post_id)
    datt =post.datt_set.all

    if request.method == 'POST':
        return redirect("posts:list")

    else:
        post_form = PostForm(instance=post)

        context={'post_form': post_form, 'datt':datt, "post":post}

    return render(request, 'datt.html', context)


def p_createdatt(request,post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        author_text= Datt(author_text=post)
        datt_form=DattForm(request.POST,instance=author_text)# POST방식으로 전송된것을 싹다 사용해서 객체로 만들어라!
        if datt_form.is_valid(): # 제대로 된 값을 입력하였다면
            datt_form.save()

            post = get_object_or_404(Post, pk=post_id)
            datt = post.datt_set.all
            post_form = PostForm(instance=post)
            context={'post_form': post_form, 'datt':datt, "post":post}
            return render(request, 'datt.html', context) #다시 돌아간다!

    # GET 방식으로 호출될때 => form action을 사용하지않는 거의 모든 방식
    else:
        datt_form=DattForm() #PostForm의 인자가 ()처럼 비어있기 때문에 비어있는 형태로 출력된다.
        return render(request, 'createdatt.html',{'datt_form':datt_form})


def p_deletedatt(request,post_id,datts_id):
    datt = Datt.objects.get(id=datts_id)
    datt.delete()

    post = get_object_or_404(Post, pk=post_id)
    datt = post.datt_set.all
    post_form = PostForm(instance=post)
    context = {'post_form': post_form, 'datt': datt, "post": post}
    return render(request, 'datt.html', context)

def p_updatedatt(request,post_id,datts_id):
    post= get_object_or_404(Post,pk=post_id)
    datt= get_object_or_404(Datt,pk=datts_id)

    if request.method == 'POST':
        datt_form = DattForm(request.POST, instance=datt)

        if datt_form.is_valid():
            datt_form.save()

            post = get_object_or_404(Post, pk=post_id)
            datt = post.datt_set.all
            post_form = PostForm(instance=post)
            context = {'post_form': post_form, 'datt': datt, "post": post}
            return render(request, 'datt.html', context)

    else:
        datt_form = DattForm(instance=datt)

    return render(request, 'createdatt.html', {'datt_form': datt_form})


# def p_createdatt(request,post_id):
#     if request.method == 'POST':
#         post = Post.objects.get(pk=post_id)
#         author_text= Datt(author_text=post)
#         datt_form=DattForm(request.POST,instance=author_text)# POST방식으로 전송된것을 싹다 사용해서 객체로 만들어라!
#         if datt_form.is_valid(): # 제대로 된 값을 입력하였다면
#             datt_form.save()
#
#             post = get_object_or_404(Post, pk=post_id)
#             datt = post.datt_set.all
#             post_form = PostForm(instance=post)
#             context={'post_form': post_form, 'datt':datt, "post":post}
#             return render(request, 'datt.html', context) #다시 돌아간다!

