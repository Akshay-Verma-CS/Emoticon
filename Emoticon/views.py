from django.shortcuts  import render
from django.http import HttpResponseRedirect
from .modules.forms import UploadFileForm
import os
from .services import EmotionService

APP_PATH = os.getcwd()
TEMP_DIR_PATH = "/Emoticon/data/tmp/"

def home(request):
    return render(request,"index.html")

def about(request):
    print("path - ",request.path)
    return render(request,"about.html")


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            responseMessage = handle_uploaded_file(request.FILES['file'])
            return render(request,"success.html",{"message" : responseMessage})
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})

def handle_uploaded_file(file):
    fileName = APP_PATH + TEMP_DIR_PATH + file.name
    with open(fileName, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    emoService = EmotionService()
    responseMessage = emoService.checkEmotion(fileName)
    os.remove(fileName)
    return responseMessage
    

def success_view(request):
    return render(request, 'success.html')


