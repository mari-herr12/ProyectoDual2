from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'AppConoce/index.html')

def PueblosMag(request):
    return render(request, 'AppConoce/PueblosMag.html')
def Museos(request):
    return render(request, 'AppConoce/Museos.html')

def Intro(request):
    return render(request, 'AppConoce/Intro.html')



def plantilla(request):
    return render(request, 'AppConoce/plantilla.html')
    

def ZonasArqueológicas(request):
    return render(request, 'AppConoce/ZonasArqueológicas.html')
    