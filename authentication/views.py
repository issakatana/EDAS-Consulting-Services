from django.shortcuts import render



def home(request):

    context = {
        
    }

    return render(request, 'home.html', context)


def aboutus(request):

    context = {
        
    }

    return render(request, 'aboutus.html', context)


def ourservices(request):

    context = {
        
    }

    return render(request, 'services.html', context)


def contact(request):

    context = {
        
    }

    return render(request, 'contact.html', context)