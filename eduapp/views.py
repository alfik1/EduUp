from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,TemplateView,FormView
from eduapp.models import Student,User
from eduapp.forms import AddStudentForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login


# Create your views here.
#used for creating the students details
class IndexView(CreateView):
    model=Student
    template_name="addstudent.html"
    form_class=AddStudentForm
    success_url=reverse_lazy("index")
    def form_valid(self, form):
        form.instance.user=self.request.user
        print(form.instance)

        return super().form_valid(form)

#for login purposes only
class LoginView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            usr = authenticate(request, username=uname, password=pwd)
            if usr:
                login(request, usr)
                
                return redirect("index")
            else:
                
                return render(request, self.template_name, {"form": form})

#To list the students details
class StudentListView(ListView):
    model=Student
    template_name="student-list.html"
    context_object_name="students"

    

    


