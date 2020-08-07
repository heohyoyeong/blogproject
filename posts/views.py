from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Datt, User
from posts.forms import PostForm, DattForm
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password


def p_list(request):
    my_list= Post.objects.all().order_by("-id")
    context={'posts':my_list}
    return render(request,'list.html',context)

def p_create(request):
    # POST 방식으로 호출될때 =>form action method="post"인 방식
    if request.method == 'POST':
        post_form=PostForm(request.POST) # POST방식으로 전송된것을 싹다 사용해서 객체로 만들어라!
        PostForm.Meta.fields.append('author' == User.id)
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


# Create your views here.
def register(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password',None)
        res_data = {}
        if not (username and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password :
            return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
        else :
            user = User(username=username, password=make_password(password))
            user.save()
        return render(request, 'index.html', res_data)


def login(request):
    response_data = {}

    if request.method == "GET" :
        return render(request, 'login.html')

    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)


        my_list = Post.objects.all().order_by("-id")
        response_data['posts'] = my_list
        response_data['user'] = login_username
        if not (login_username and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else :
            myuser = User.objects.get(username=login_username)
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(login_password, myuser.password):
                request.session['users'] = myuser.username

                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return render(request,'list.html', response_data)
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."
                return render(request, 'index.html')