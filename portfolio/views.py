from django.shortcuts import render


def portfolio_homepage(request):
    return render(request, 'portfolio/index.html')

