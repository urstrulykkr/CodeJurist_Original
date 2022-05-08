from multiprocessing import context
from re import template
from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .models import *
from compiler.views import *
from django.contrib.auth.models import User, auth

def home(request):
    questions = Problems.objects.all()
    return render(request, 'home.html', {'questions': questions})

def leaderboard(request):
    return render(request, 'leaderboard.html')

def problem(request, var_id):
    question = Problems.objects.get(id=var_id)
    type_comp = ['None', 'Python', 'C++', 'Java']
    context = {
        'var0': question.id,
        'var1': question.problem_statement,
        'var2': type_comp
    }
    return render(request, 'problem.html', context)

def submit(request, variable_id):
    if request.POST['type'] == 'Python':
        output = compile_with_python(request, variable_id)
    if request.POST['type'] == 'C++':
        output = compile_with_c(request, variable_id)
    if request.POST['type'] == 'Java':
        output = compile_with_java(request, variable_id)
    context = {
        'output' : output,
    }
    
    return render(request, 'leaderboard.html', context)

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if password1 == '':
                return HttpResponse('Please enter a password')
            elif User.objects.filter(email=email).exists():
                return HttpResponse('Email already exists...')
            else:
                user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, email=email, password= password1)
                user.save()
            return HttpResponse('User saved successfully...')
        else:
            return HttpResponse('Password not matching...')
        redirect('/')
    else:    
        return HttpResponse('you are registered')
