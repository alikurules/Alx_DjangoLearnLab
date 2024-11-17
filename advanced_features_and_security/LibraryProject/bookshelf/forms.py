from django import forms

class ExampleForm(forms.Form):
    """
    A sample form for demonstration purposes.
    """
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)
