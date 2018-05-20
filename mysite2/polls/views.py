
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Document
from .forms import DocumentForm


def home(request):
    documents = Document.objects.all()#資料庫裡所有的資料
    return render(request, 'core/home.html', { 'documents': documents })#執行home.html並把documents一起帶進去


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')#執行simple_upload.html


def model_form_upload(request):#model_form_upload.html的執行內容
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })#執行model_form_upload.html並把form一起帶進去
