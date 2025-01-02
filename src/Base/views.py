from django.shortcuts import render

def base_plate(request):
    context = {
        'title': 'None',
        'message': '200',
    }
    return render(request, 'index.html', context)


