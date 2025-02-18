from django import forms

# Define a form for the first page
class StudentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    roll = forms.CharField(label='Roll', max_length=50)
    subjects = forms.ChoiceField(label='Subjects', choices=[
        ('Math', 'Math'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('History', 'History'),
    ])
