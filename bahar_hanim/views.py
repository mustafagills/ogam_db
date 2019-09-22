from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from project_item.models import Proje
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
@login_required
def homepage(request):
    projes = Proje.objects.all().order_by('id')
    return render(request, 'homepage.html', {'projes': projes})

@login_required
def search_results(request):
    queryset_list = Proje.objects.all()
    search_option = request.GET.get('search_option')
    parameter = request.GET.get('parameter')
    if search_option == "proje_kod":
        queryset_list = queryset_list.filter(proje_kod=parameter) or []
        return render(request, 'homepage.html', {'projes': queryset_list})
    if search_option == "proje_adi":
        queryset_list = queryset_list.filter(proje_adi__icontains=parameter) or []
        return render(request, 'homepage.html', {'projes': queryset_list})
    if search_option == "proje_yoneticisi":
        queryset_list = queryset_list.filter(proje_yoneticisi=parameter) or []
        return render(request, 'homepage.html', {'projes': queryset_list})
    if search_option == "proje_calisanlar_no":
        queryset_list = queryset_list.filter(proje_calisanlar_no=parameter) or []
        return render(request, 'homepage.html', {'projes': queryset_list})
    if search_option == "proje_teknik_yonetici_no":
        queryset_list = queryset_list.filter(proje_teknik_yonetici_no=parameter) or []
        return render(request, 'homepage.html', {'projes': queryset_list})
@login_required
def project_detail(request, pk):
    proje = get_object_or_404(Proje, pk=pk)
    return render(request, 'details.html', {'proje': proje })
