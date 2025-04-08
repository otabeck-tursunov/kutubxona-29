from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime

from .models import *
from .forms import *


def hello_view(request):
    return HttpResponse("Hello, Django!")


def home_view(request):
    now = datetime.now()
    context = {
        'now': now,
    }
    return render(request, 'home.html', context)


def talabalar_view(request):
    if request.method == "POST":
        form_data = TalabaForm(request.POST)
        if form_data.is_valid():
            data = form_data.cleaned_data
            Talaba.objects.create(
                ism=data['ism'],
                guruh=data['guruh'],
                kurs=data['kurs'],
                kitob_soni=data['kitob_soni']
            )
            return redirect('talabalar')
        return HttpResponse(f"{form_data.errors}")
    talabalar = Talaba.objects.order_by('ism')
    context = {
        'talabalar': talabalar,
        'talaba_form': TalabaForm,
    }
    return render(request, 'talabalar.html', context)


def talaba_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        'talaba': talaba,
    }
    return render(request, 'talaba.html', context)


def talaba_update_view(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)
    if request.method == "POST":
        form_data = TalabaForm(request.POST, instance=talaba)
        if form_data.is_valid():
            form_data.save()
            return redirect('talabalar')
        return HttpResponse(f"{form_data.errors}")
    context = {
        "talaba": talaba,
        "form": TalabaForm(instance=talaba),
    }
    return render(request, 'talaba-update.html', context)


def bitiruvchilar_view(request):
    talabalar = Talaba.objects.filter(kurs=4)
    context = {
        'talabalar': talabalar,
    }
    return render(request, 'bitiruvchilar.html', context)


def mualliflar_view(request):
    mualliflar = Muallif.objects.all()
    if request.method == "POST":
        form_data = MuallifForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('mualliflar')
        return HttpResponse(f"Xatolik xabar: \n{form_data.errors}")
    context = {
        'mualliflar': mualliflar,
        'form': MuallifForm,
    }
    return render(request, 'mualliflar.html', context)


def muallif_post_view(request):
    if request.method == "POST":
        Muallif.objects.create(
            ism=request.POST.get('ism'),
            jins=request.POST.get('jins'),
            t_sana=request.POST.get('t_sana') if request.POST.get('t_sana') else None,
            kitob_soni=request.POST.get('kitob_soni') if request.POST.get('kitob_soni') else None,
            tirik=True if request.POST.get('tirik') == "on" else False
        )
        return redirect('mualliflar')
    return render(request, 'muallif_post.html')


def kitoblar_view(request):
    if request.method == "POST":
        data = KitobForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('kitoblar')
        return HttpResponse(f"Xatolik xabar: \n{data.errors}")
    kitoblar = Kitob.objects.all()
    context = {
        'kitoblar': kitoblar,
        'mualliflar': Muallif.objects.all(),
        'form': KitobForm,
    }
    return render(request, 'kitoblar.html', context)


def kitob_view(request, pk):
    kitob = get_object_or_404(Kitob, pk=pk)
    context = {
        'kitob': kitob,
    }
    return render(request, 'kitob.html', context)


def kitob_update_view(request, pk):
    kitob = get_object_or_404(Kitob, pk=pk)
    if request.method == "POST":
        kitob.nom = request.POST.get('nom')
        kitob.janr = request.POST.get('janr')
        kitob.sahifa = request.POST.get('sahifa')
        kitob.muallif = Muallif.objects.get(id=request.POST.get('muallif_id'))
        kitob.save()
        return redirect('kitoblar')
    mualliflar = Muallif.objects.all()
    context = {
        'kitob': kitob,
        'mualliflar': mualliflar,
    }
    return render(request, 'kitob-update.html', context)
