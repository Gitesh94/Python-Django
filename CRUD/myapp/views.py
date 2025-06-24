from django.shortcuts import render, redirect
from .models import *
from .forms import InformationForm
# Create your views here.

def infoView(request):
    allInfo = Information.objects.all() 
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        info = Information.objects.create(name=name, email=email).save()
    return render(request, 'addinfo.html', {'allInfo':allInfo})

def deleteView(request, id):
    dlt = Information.objects.get(id=id)
    dlt.delete()
    return redirect('info')

def updateView(request, id):
    if request.method == 'POST':
        editForm = Information.objects.get(id=id)
        form = InformationForm(request.POST, instance=editForm)
        if form.is_valid():
            form.save()
            return redirect('info')
    editForm = Information.objects.get(id=id)
    form = InformationForm(instance=editForm)
    return render(request, 'update.html', {'form': form})
