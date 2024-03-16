from django.shortcuts import render

def index(request):
    return render(request, 'pages/home.html')
def aboutPage(request):
    return render(request, 'pages/about.html')
