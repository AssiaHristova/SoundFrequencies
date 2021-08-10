from django.shortcuts import render


def about_page(request):
    return render(request, 'general/about_us.html')


def contacts_page(request):
    return render(request, 'general/contact_us.html')
