from django.shortcuts import render
from mainsite.models import *
from mainsite.forms import *
from django.shortcuts import redirect

# Create your views here.
def mainpage(request):
    return render(request, "index.html", locals())

def skazki(request):
    return render(request, "skazki_lar.html", locals())

def skazki_dar(request):
    return render(request, "skazki_dar.html", locals())

def risunki(request):
        return render(request, "risunki.html", locals())

def admin_page(request):
    return render(request, "admin/admin_page.html", locals())

def admin_page_skazki(request):
    skazka_list = skazka_dar.objects.all()
    return render(request, "admin/admin_page_skazki.html", locals())

def add_skazka(request):
    return render(request, "admin/admin_page.html", locals())

def change_skazka(request, id_skazka):
    skazka = skazka_dar.objects.get(id_skazka=id_skazka)
    form = skazka_form(instance=skazka)
    if request.method == "POST":
        if 'good' in request.POST.keys() and request.POST['good']:
            form = skazka_form(request.POST, request.FILES, instance=skazka)
            if form.is_valid():
                form.save()
                return redirect("admin_page_skazki")
            else:
                return redirect("change_skazka")
        else:
            return redirect("admin_page_skazki")
    return render(request, "admin/change_skazka.html", locals())


def delete_skazka(request, id_skazka):
    skazka = skazka_dar.objects.get(id_skazka=id_skazka)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            skazka.delete()
            return redirect("admin_page_skazki")
        else:
            return redirect("admin_page_skazki")
    return render(request, "admin/delete_skazka.html", locals())