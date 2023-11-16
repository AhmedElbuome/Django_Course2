from django.shortcuts import render
from .forms import LoginForm

def index(request):
    
    return render(request, 'pages/index.html', {'name':'mohamed'})

def about(request):
    
    if request.method == 'POST':
    
        dateform = LoginForm(request.POST)
    
        if dateform.is_valid():
            
            dateform.save()
    # username = request.POST.get("username")
    # password = request.POST.get("password")
    # date = Login(username = username, password = password)
    # # date.save()
    
    return render(request, 'pages/about.html', {'lf':LoginForm})

