from django.shortcuts import render, redirect, get_object_or_404
from .models import todo_db
from .forms import todo_form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

#------General home page ----------#

def home(request):
    return render(request,'index.html')

#----------signup ---------------#

def signup_user(request):
    if request.method=='GET':
       return render(request,'signup_user.html',{'form':UserCreationForm()})

    else:
       if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('current_todo')
            except IntegrityError:
                return render(request,'signup_user.html',{'form':UserCreationForm(),'error':'Username has already taken.'})

       else:
        return render(request,'signup_user.html',{'form':UserCreationForm(),'error':'password not match'})

#------------login--------------------#

def login_user(request):
    if request.method=='GET':
       return render(request,'login_user.html',{'form':AuthenticationForm()})

    else:
       user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
       if user is None:
            return render(request,'login_user.html',{'form':AuthenticationForm(),'error':'Username and password did not match'})
       else:
            login(request,user)
            return redirect('current_todo')

#------------logout-------------------#

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


#------- User home page or current todo page--------#


@login_required
def current_todo(request):

        data=todo_db.objects.filter(user=request.user,completed_date__isnull=True)
        return render(request,'current_todo.html',{'todo_data':data})

#------- completed todo page--------#


@login_required
def completed_todo(request):

        data=todo_db.objects.filter(user=request.user,completed_date__isnull=False).order_by('-completed_date')
        return render(request,'completed_todo.html',{'todo_data':data})


#------- create todo page--------#


@login_required
def create_todo(request):

        if request.method=="GET":
          return render(request,'create_todo.html',{'form':todo_form()})

        else:
            try:
                form=todo_form(request.POST)
                new_todo=form.save(commit=False)
                new_todo.user=request.user
                new_todo.save()
                return redirect('current_todo')
            except ValueError:
                return render(request,'create_todo.html',{'form':todo_form(),'error':"Invalid data passed In.Please try again"})


#-------show todo---------------#


@login_required
def show_todo(request,todo_pk):

        data=get_object_or_404(todo_db, pk=todo_pk, user=request.user)
        if request.method=="GET":
            form=todo_form(instance=data)
            return render(request,'show_todo.html',{'todo_data':data,'form':form})

        else:
            try:
                form=todo_form(request.POST,instance=data)
                form.save()
                return redirect('current_todo')
            except ValueError:
                return render(request,'show_todo.html',{'todo_data':data,'form':form,'error':"data not valid"})

#-------complete todo---------------#

@login_required
def complete_todo(request,todo_pk):

        data=get_object_or_404(todo_db, pk=todo_pk, user=request.user)
        data.completed_date=timezone.now()
        data.save()
        return redirect('completed_todo')

#-------Delete todo---------------#

@login_required
def delete_todo(request,todo_pk):

        data=get_object_or_404(todo_db, pk=todo_pk, user=request.user)
        data.delete()
        return redirect('current_todo')
