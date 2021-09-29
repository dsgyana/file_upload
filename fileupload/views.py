from django.shortcuts import render, HttpResponse
from .models import fileUpload

# Create your views here.


def home(request):
    if request.method == 'POST':
        file2 = request.FILES['file']
        document = fileUpload.objects.create(file=file2)
        document.save()
        return HttpResponse("Uploaded Success")
    return render(request, 'index.html')