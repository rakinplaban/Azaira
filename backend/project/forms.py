from django import forms

class InputForm(forms.Form):
    input = forms.CharField(label="Title",widget=forms.TextInput(attrs={
        "class" : "form-control"
    })),
    search = forms.CharField(label="Search",widget=forms.TextInput(attrs={
        "class" : "form-control"
    })),