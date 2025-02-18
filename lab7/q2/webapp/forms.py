from django import forms

# Create a form for the input fields
class UserDetailsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    roll = forms.CharField(label='Roll', max_length=100)
    subject = forms.ChoiceField(label='Subject', choices=[
        ('Math', 'Math'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('History', 'History'),
        ('Geography', 'Geography'),
    ])
