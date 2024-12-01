from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    event_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  
    event_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))  
    ratings = forms.ChoiceField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    feedback = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=20)  
