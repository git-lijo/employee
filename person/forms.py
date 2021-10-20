from django import forms
from .models import EmployeeData


class PostForm(forms.ModelForm):
    class Meta:
        model = EmployeeData
        fields = ('EmpName', 'EmpMail', 'Password', 'PhoneNumber', 'Address')
        widgets = {
            'EmpName': forms.TextInput(attrs={'class': 'form-control'}),
            'EmpMail': forms.EmailInput(attrs={'class': 'form-control'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'PhoneNumber': forms.NumberInput(attrs={'class': 'form-control'}),
            'Address': forms.Textarea(attrs={'class': 'form-control'}),
        }



