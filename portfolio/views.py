from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile

def main(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        obj = Profile.objects
        all_obj = obj.all()
        if not username and not password:
            return HttpResponse("please fill this fields")
        else:
            is_prime = False
            for one in all_obj:
                if one.username == username and one.password == password:
                    is_prime = True
                    request.session["username"] = one.username
            if not is_prime:
                return HttpResponse("name or password is wrong")                    
    if "username" in request.session:
        context = {"username": request.session["username"]}
        return render(request, "main.html", context=context)
    else:
        return render(request, "main.html", context=None)


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, "project.html") 


def skill(request):
    return render(request, "skills.html") 


def contact(request):
    return render(request, "contact.html") 


def login(request):
    if request.method == "POST":
        username = request.POST.get("name2")
        password = request.POST.get("password2")
        all_obj = Profile.objects.all()
        username_lst = []
        password_lst = []
        for obj in all_obj:
            username_lst.append(obj.username)
            password_lst.append(obj.password)
        if not username and not password:
            return HttpResponse("please fill this fields")
        elif not username in username_lst and not password in password_lst:
            Profile.objects.create(username=username, password=password)
        else:
            return HttpResponse("this name or password is already in use")
    return render(request, "login.html")


def registration(request):
    return render(request, "register.html")


def logout(request):
    try:
        request.session.pop("username")
    except:
        return HttpResponse("you can not log out")
    return redirect("/")

    