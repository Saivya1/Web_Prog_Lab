from django.shortcuts import render

# View to display the form
def car_form(request):
    if request.method == 'POST':
        manufacturer = request.POST.get('manufacturer')
        model_name = request.POST.get('model')
        return render(request, 'webapp/display.html', {'manufacturer': manufacturer, 'model_name': model_name})
    return render(request, 'webapp/car_form.html')
