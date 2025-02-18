from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserDetailsForm

def first_page(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            # Store the data in session
            name = form.cleaned_data['name']
            roll = form.cleaned_data['roll']
            subject = form.cleaned_data['subject']
            
            request.session['name'] = name
            request.session['roll'] = roll
            request.session['subject'] = subject
            
            # Redirect to the second page
            return redirect('second_page')
    else:
        form = UserDetailsForm()

    return render(request, 'webapp/firstPage.html', {'form': form})

def second_page(request):
    # Get the data from session
    name = request.session.get('name', 'Not available')
    roll = request.session.get('roll', 'Not available')
    subject = request.session.get('subject', 'Not available')

    return render(request, 'webapp/secondPage.html', {'name': name, 'roll': roll, 'subject': subject})
