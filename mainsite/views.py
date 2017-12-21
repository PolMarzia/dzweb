from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, "index.html", locals())

def skazki(request):
    return render(request, "skazki_lar.html", locals())

def skazki_dar(request):
    return render(request, "skazki_dar.html", locals())

def risunki(request):
        return render(request, "risunki.html", locals())