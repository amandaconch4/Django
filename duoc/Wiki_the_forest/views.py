from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request, 'menuprincipal_wiki.html', {})

def foro(request):
    return render(request, 'forowiki.html', {})

def registro(request):
    return render(request, 'registrase_wiki.html', {})

def login(request):
    return render(request, 'inicio_sesion_wiki.html', {})

def cuenta(request):
    return render(request, 'micuentatf.html', {})