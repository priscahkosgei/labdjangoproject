from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def Mygallery(request):
    return render(request,'Gallery.html')
def aboutus(request):
    return render(request,'about.html')
def contactus(request):
    return render(request,'contact.html')