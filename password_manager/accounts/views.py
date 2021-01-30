from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm, AccountUpdateForm




# Create your views here.
def login_page_view(request):
    context = {}
    account = request.user
    if account.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            account = authenticate(email=email, password=password)
            if account:
                login(request, account)
                return redirect("home")
        else:
            context['form'] = form
    else:
        form = LoginForm()
        context['form'] = form
    return render(request, "login.html", context)


def register_page_view(request):
    context = {}
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        account = authenticate(email=email, password=password)
        login(request, account)
        return redirect("home")

    context['form'] = form
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect("welcome")


def account_page_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("accounts:login")

    form = AccountUpdateForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        context['msg'] = "Profile Updated!"
        form = AccountUpdateForm(initial={
            'email':user.email,
            'username':user.username,
        })
    context['form'] = form
    return render(request, "account.html", context)


def must_authenticate_view(request):
    return render(request, 'must_authenticate.html', {})


def unauthorized_view(request):
    return render(request, 'unauthorized_view.html', {})
