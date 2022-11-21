from django.shortcuts import render
from CRUDOperation.models import DiseaseType
from django.contrib import messages
from CRUDOperation.forms import DiseaseTypeforms
from django.http import HttpResponseRedirect, HttpResponseNotFound

def showDiseaseType(request):
  showall = DiseaseType.objects.all()
  return render(request, 'index.html',  {"data": showall})

def InsertDiseaseType(request):
  if request.method == "POST":
    if request.POST.get('diseasetype_id') and request.POST.get('diseasetype_description'):
      saverecord = DiseaseType()
      saverecord.diseasetype_id = request.POST.get('diseasetype_id')
      saverecord.diseasetype_description = request.POST.get('diseasetype_description')
      saverecord.save()
      messages.success(request, 'DiseaseType' + saverecord.diseasetype_id + 'is saved successfully!')
      return render(request, 'insert.html')
  else:
    return render(request, 'insert.html')

def EditDiseaseType(request, diseasetype_id):
  editDiseaseTypeobj = DiseaseType.objects.get(diseasetype_id=diseasetype_id)
  return render(request, 'edit.html', {"DiseaseType":editDiseaseTypeobj})

def UpdateDiseaseType(request, diseasetype_id):
  updateDiseaseType = DiseaseType.objects.get(diseasetype_id = diseasetype_id)
  form =DiseaseTypeforms(request.POST, instance=updateDiseaseType)
  if form.is_valid():
    form.save()
    messages.success(request, "Record updated successfully")
    return render(request, 'edit.html', {"DiseaseType":updateDiseaseType})

def DelDiseaseType(request, diseasetype_id):
  delDiseaseType = DiseaseType.objects.get(diseasetype_id=diseasetype_id)
  delDiseaseType.delete()
  #showdata = DiseaseType.objects.all()
  # return render(request, 'index.html', {"data": showdata})
  return HttpResponseRedirect("/")