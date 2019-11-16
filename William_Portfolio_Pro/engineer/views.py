from django.shortcuts import render

def engineer(request):
    return render(request, 'engineer.html', {})

def resume(request):
    return render(request, 'resume.html', {})
