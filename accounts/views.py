from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is already taken")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is being used")
                    return redirect("register")
                else:
                    newuser = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    # auth.login(request, newuser)
                    # messages.success(request, "You're logged in")
                    newuser.save()
                    messages.success(request, "You're now registered")
                    return redirect("login")
        else:
            messages.error(request, "Passwords don't match")
            return redirect("register")
    else:
        return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You've logged in")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, "accounts/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You've logged out")
    return redirect("index")


def dashboard(request):
    usercontacts = Contact.objects.order_by("-contactdate").filter(userid=request.user.id)
    return render(request, "accounts/dashboard.html", {"contacts": usercontacts})
