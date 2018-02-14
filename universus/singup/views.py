from django.shortcuts import render
from .forms import SingupForm

def singup(request):
   name = "---"
   surname = "---"
   if request.method == "POST":
      #Get the posted form
      form = SingupForm(request.POST)

      if form.is_valid():
         name = form.cleaned_data["name"]
         surname = form.cleaned_data["surname"]
         email = form.cleaned_data["email"]
         password = form.cleaned_data["password"]
         return render(request, 'singup/success_singup.html', locals())
   else:
      form = SingupForm()   
   return render(request, 'singup/singup.html', locals())
