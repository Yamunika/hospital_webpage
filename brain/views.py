from django.shortcuts import render

# Create your views here.
def doctor(request):
    return render(request,'brain1.html')

def doctor1(request):
    return render(request,'brain2.html')