from django.shortcuts import render, redirect
from .forms import StudentForm

def first_page(request):
    if request.method == 'POST':
        # Create an instance of the form with POST data
        form = StudentForm(request.POST)
        if form.is_valid():
            # Store the data in the session
            request.session['name'] = form.cleaned_data['name']
            request.session['roll'] = form.cleaned_data['roll']
            request.session['subjects'] = form.cleaned_data['subjects']
            
            # Redirect to the second page
            return redirect('second_page')
    else:
        form = StudentForm()

    return render(request, 'webapp/firstPage.html', {'form': form})


def second_page(request):
    # Retrieve the data from session
    name = request.session.get('name', 'Not available')
    roll = request.session.get('roll', 'Not available')
    subjects = request.session.get('subjects', 'Not available')

    # Send the data to the second page
    return render(request, 'webapp/secondPage.html', {
        'name': name,
        'roll': roll,
        'subjects': subjects,
    })
