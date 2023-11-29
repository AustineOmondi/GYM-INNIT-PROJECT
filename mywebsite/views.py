from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, "home.html", {})
def contact(request):
    if request.method == "POST":
        Name = request.POST.get("Name")
        Email = request.POST.get("Email")
        Website = request.POST.get("Website")
        Comment = request.POST.get("Comment")

        send_mail(
            Name,
            Email,
            Website,
            Comment,
            { 'andnnd@gmail.com'},


        )

        return render(request, "contact.html", {"Name": Name})
    else:
        return render(request, "contact.html", {})
def about(request):
    return render(request, "about-us.html", {})
def class_details(request):
    return render(request, "class-details.html", {})
def services(request):
    return render(request, "services.html", {})
def team(request):
    return render(request, "team.html", {})
def blog(request):
    return render(request, "blog.html", {})
def gallery(request):
    return render(request, "gallery.html", {})

# Create your views here.
