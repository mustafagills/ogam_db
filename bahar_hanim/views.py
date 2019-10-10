from django.shortcuts import render, get_object_or_404
from project_item.models import Proje
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    projes = Proje.objects.all().filter(is_archive=0)
    archives = Proje.objects.all().filter(is_archive=1)
    context = {'projes': projes.order_by('proje_kod'), 'archives': archives.order_by('proje_kod')}
    return render(request, 'homepage.html', context)

@login_required
def search_results(request):
    queryset_list = Proje.objects.all()
    search_option = request.GET.get('search_option')
    parameter = request.GET.get('parameter')
    if search_option == "proje_kod":
        try:
            parameter = int(parameter)
        except ValueError:
            return render(request, 'homepage.html')
        queryset_list_active = queryset_list.filter(proje_kod=parameter, is_archive=0) or []
        queryset_list_archive = queryset_list.filter(proje_kod=parameter, is_archive=1) or []
        context = {
            'projes': queryset_list_active,
            'archives': queryset_list_archive,
        }
        return render(request, 'homepage.html', context)
    if search_option == "proje_yoneticisi":
        try:
            parameter = int(parameter)
        except ValueError:
            return render(request, 'homepage.html')
        queryset_list_active = queryset_list.filter(proje_yoneticisi=parameter, is_archive=0) or []
        queryset_list_archive = queryset_list.filter(proje_yoneticisi=parameter, is_archive=1) or []
        context = {
            'projes': queryset_list_active,
            'archives': queryset_list_archive,
        }
        return render(request, 'homepage.html', context)
    if search_option == "proje_teknik_yonetici_no":
        try:
            parameter = int(parameter)
        except ValueError:
            return render(request, 'homepage.html')
        queryset_list_active = queryset_list.filter(proje_teknik_yonetici_no=parameter, is_archive=0) or []
        queryset_list_archive = queryset_list.filter(proje_teknik_yonetici_no=parameter, is_archive=1) or []
        context = {
            'projes': queryset_list_active,
            'archives': queryset_list_archive,
        }
        return render(request, 'homepage.html', context)
    if search_option == "proje_durumu":
        try:
            parameter = int(parameter)
        except ValueError:
            return render(request, 'homepage.html')
        queryset_list_active = queryset_list.filter(proje_durumu=parameter, is_archive=0) or []
        queryset_list_archive = queryset_list.filter(proje_durumu=parameter, is_archive=1) or []
        context = {
            'projes': queryset_list_active,
            'archives': queryset_list_archive,
        }
        return render(request, 'homepage.html', context)
    if search_option == "proje_status":
        try:
            parameter = int(parameter)
        except ValueError:
            return render(request, 'homepage.html')
        queryset_list_active = queryset_list.filter(proje_status=parameter, is_archive=0) or []
        queryset_list_archive = queryset_list.filter(proje_status=parameter, is_archive=1) or []
        context = {
            'projes': queryset_list_active,
            'archives': queryset_list_archive,
        }
        return render(request, 'homepage.html', context)
    if search_option == "proje_tipi":
        try:
            parameter = int(parameter)
        except ValueError:
            return render(request, 'homepage.html')
        queryset_list_active = queryset_list.filter(proje_tipi=parameter, is_archive=0) or []
        queryset_list_archive = queryset_list.filter(proje_tipi=parameter, is_archive=1) or []
        context = {
            'projes': queryset_list_active,
            'archives': queryset_list_archive,
        }
        return render(request, 'homepage.html', context)
    if search_option == "proje_calisanlar_no":
        queryset_list_active = queryset_list.filter(proje_calisanlar_no__icontains=parameter, is_archive=0) or []
        queryset_list_archive = queryset_list.filter(proje_calisanlar_no__icontains=parameter, is_archive=1) or []
        context = {
            'projes': queryset_list_active,
            'archives': queryset_list_archive,
        }
        return render(request, 'homepage.html', context)
    if search_option == "proje_adi":
        queryset_list_active = queryset_list.filter(proje_adi__icontains=parameter, is_archive=0) or []
        queryset_list_archive = queryset_list.filter(proje_adi__icontains=parameter, is_archive=1) or []
        context = {
            'projes': queryset_list_active,
            'archives': queryset_list_archive,
        }
        return render(request, 'homepage.html', context)
@login_required
def project_detail(request, pk):
    proje = get_object_or_404(Proje, pk=pk)
    return render(request, 'details.html', {'proje': proje })
