from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
import os


data={}

def signin_page(request):
    return render(request,'signin_page.html')

def signup_page(request):
    return render(request,'signup_page.html')

def index(request):
    return render(request,'index.html')

def forgot_password(request):
    return render(request,'forgot_password.html')

def profile_page(request):
    return render(request,'profile_page.html')




#signup_functionality
def signup(request):
    if request.method=="POST":
        try:
            user=Master.objects.get(Email=request.POST['email'])
            msg="User Alredy Exist!!!!"
            return render(request,'signup_page.html',{'msg':msg})
        except:
            password = request.POST['password']
            if password == request.POST['confirm_password']:
                master = Master.objects.create(Email = request.POST['email'],Password = password)
                print('Signup successfully.')
                return render(request,'signin_page.html')
            else:
                msg='both password should be same.'
                return render(request,'signup_page.html',{'msg':msg})
    else:
        return render(request,'signup_page.html')

def signin(request):
    print(request.POST)
    try:
        master = Master.objects.get(Email = request.POST['email'])
        if master.Password == request.POST['password']:
            request.session['email'] = master.Email
            return redirect(index)

        else:
            return render(request, "signin_page.html",{'error':"Password does not match"})
    except Master.DoesNotExist as err:
        return render(request,"signin_page.html",{'error':"User does not Exists Please SignUp"})

# profile page 
def profile_page(request):
    print(request.session['email'])
    if 'email' in request.session:
        try:
            try:
                profile_data(request)
                return render(request,'profile_page.html',data)
            except:
                profile_data(request)
                return redirect(index)
        except Exception as err:
            print("data not availabe ! submit your data admin side & relogin")
    return redirect(index)


def profile_data(request):
    master = Master.objects.get(Email = request.session['email'])
    user_profile = Common.objects.get(Master = master)

    user_profile.first_name = user_profile.Name.split()[0]
    user_profile.last_name = user_profile.Name.split()[1]
    user_profile.Address = user_profile.Address


    user_profile.DateOfBirth = user_profile.DateOfBirth.strftime("%Y-%m-%d")
    user_profile.DateOfJoining = user_profile.DateOfJoining.strftime("%Y-%m-%d")

    data['user_data'] = user_profile
    
    return redirect(profile_page)

main_path = settings.MEDIA_ROOT

# profile update functionality student
def profile_update(request):
    print(request.POST)
    master = Master.objects.get(Email = request.session['email'])
    user_profile = Common.objects.get(Master = master)


    user_profile.Name =' '.join([request.POST['first_name'], request.POST['last_name']])
    user_profile.DateOfBirth = request.POST['dateofbirth']
    user_profile.DateOfJoining = request.POST['dateofjoining']
    user_profile.Address = request.POST['address']
     
    file_path = os.path.join(main_path, 'profiles')


    user_profile.save()

    return redirect(profile_page)

# Delete account Functionality
def delete_account_function(request):
    print(request.POST)
    master=Master.objects.get(Email = request.session['email'])
    master.delete()
    return redirect(signup)

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect(signin_page)

    return redirect(signup_page)