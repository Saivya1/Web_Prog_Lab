from django.shortcuts import render

def home_page(request):
    return render(request, 'webapp/home_page.html')

def metadata_page(request):
    return render(request, 'webapp/metadata_page.html')

def reviews_page(request):
    return render(request, 'webapp/reviews_page.html')

def publisher_page(request):
    return render(request, 'webapp/publisher_page.html')
