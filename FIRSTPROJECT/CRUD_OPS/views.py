from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import register
from CRUD_OPS import forms
from .forms import registerform

# Create your views here.
def register_view(request):
    #form=forms.registerform
    if request.method=="POST":
        form=forms.registerform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("success")
            except:
                print('Error saving details')
    else:
        form=forms.registerform
    return render(request,"CRUD_OPS/register.html",{"form":form})

def success(request):
    people=register.objects.all()
    return render(request,'CRUD_OPS/success.html',{'people':people})

def destroy(request, id):
    people=register.objects.get(id= id)
    people.delete()
    return redirect("success")

def edit(request, id):
    people=register.objects.get(id= id)
    return render(request,"CRUD_OPS/edit.html",{'people':people})

def update(request, id):
    person=register.objects.get(id= id)
    form = registerform(request.POST, instance=person)
    if form.is_valid():
        try:
            form.save()
            return redirect("success")
        except:
            print('Error saving details')
    return render(request,"CRUD_OPS/edit.html",{"person":person})    