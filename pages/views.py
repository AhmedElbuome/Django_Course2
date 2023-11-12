from django.shortcuts import render

def index(request):
    
    return render(request, 'pages/index.html', {'name':'mohamed'})

def about(request):
    
    return render(request, 'pages/about.html')