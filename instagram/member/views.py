from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as django_login

from .forms import SignupForm, LoginForm

User = get_user_model()


def login(request):
    # POST 요청(Form submit)의 경우
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('post_list')

    else:
        # GET요청에서는 Form을 보여줌
        form = LoginForm()
    context = {
        'login_form': form,
    }
    return render(request, 'member/login.html', context)


def logout(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']


def signup(request):
    if request.method == "POST":
        # 데이터가 binding된 SignupForm인스턴스를 생성
        form = SignupForm(request.POST)
        # 해당 form이 자신의 필드에 유효한 데이터를 가지고 있는지 유효성 검사
        if form.is_valid():
            user = form.signup()
            print(user)
            return HttpResponse(f'{user.username}, {user.password}')

    # GET 요청시 SignupForm인스턴스를 form 변수에 할당 context에 같은 키/값으로 전달
    else:
        form = SignupForm()
    context = {
        'signup_form': form
    }
    return render(request, 'member/signup.html', context)
