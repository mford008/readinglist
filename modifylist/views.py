from django.shortcuts import render

def homepage(request):
    context = {
        'message': 'hello'
    }
    return render(request, 'homepage.html', context)
