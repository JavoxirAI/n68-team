from django.shortcuts import render, redirect

from apps.pages.forms import ContactForm
from apps.pages.models import AboutPageModel


def home_page_view(request):
    return render(request, 'home.html')

def contact_page_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:contact')
        else:
            errors = []
            for key, value in form.errors.items():
                for error in value:
                    errors.append(error)
            context = {
                "errors": errors
            }
            return render(request, 'pages/contact.html', context)

    else:
        return render(request, 'pages/contact.html')

def n404_page_view(request):
    return render(request, 'pages/404.html')

def about_us_page_view(request):
    about = AboutPageModel.objects.all()

    context = {
        'about': about,
    }
    return render(request, 'pages/about-us.html', context)

def user_wishlist_page_view(request):
    return render(request, 'pages/user-wishlist.html')