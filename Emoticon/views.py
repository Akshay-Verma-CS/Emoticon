from django.shortcuts  import render
from django.http import HttpResponseRedirect
from .modules.forms import UploadFileForm
import os

APP_PATH = os.getcwd()

def home(request):
    return render(request,"index.html")


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            # Redirect to a success page or render a success message
            return HttpResponseRedirect('/success/')
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})

def handle_uploaded_file(file):
    with open(APP_PATH+'/Emoticon/data/tmp/' + file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def success_view(request):
    return render(request, 'success.html')


