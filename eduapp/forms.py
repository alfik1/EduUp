from django import forms
from eduapp.models import Student


class AddStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=["student_name", "age","mobile","profile_img","email"]

        widget={
            "student_name":forms.TextInput(attrs={"class":"form-control"}),
            "age":forms.TextInput(attrs={"class":"form-control"}),
            "mobile":forms.NumberInput(attrs={"class":"form-control"}),
            "profile_img":forms.FileInput(attrs={"class":"form-select"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control "}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
