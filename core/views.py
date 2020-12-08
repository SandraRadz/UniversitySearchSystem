from django.shortcuts import render


# Create your views here.


def index(request):
    context = {'title': 'Знайди університет мрії'}
    return render(request, 'core/home.html', context=context)
