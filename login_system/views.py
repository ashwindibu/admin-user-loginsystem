from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from . forms import RegisterationForm
from django.contrib.auth import authenticate,login,logout
from hashlib import sha256
# Create your views here.
posts= [
    {'name':'G-class','price':'10000000','img':'https://assets.newatlas.com/dims4/default/6fcf387/2147483647/strip/true/crop/1619x1079+0+0/resize/1200x800!/quality/90/?url=http%3A%2F%2Fnewatlas-brightspot.s3.amazonaws.com%2Farchive%2Fmercedes-g63-amg-6.jpg'},
    {'name':'Maserati','price':'22900000','img':'https://cdni.autocarindia.com/Utils/ImageResizer.ashx?n=https://cdni.autocarindia.com/ExtraImages/20200810074017_Maserati-Quattroporte-trofeo-static.jpg&w=700&q=90&c=1'},
    {'name':'Koenigsegg','price':'10000000','img':'https://pictures.topspeed.com/IMG/crop/202011/koenigsegg-wants-you-1_800x0w.jpg'},
    {'name':'McLaren 720S','price':'10000000','img':'https://cdn.motor1.com/images/mgl/kpOLY/s3/mclaren-720s-daniel-ricciardo-edition.jpg'},
]





def user_login(request):
    if request.user.is_authenticated:
        return redirect(homepage)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            user_block = User.objects.get(username=username)
            if user_block.is_staff == 0:
                login(request,user)
                return redirect(homepage)
            else:
                messages.error(request,'User is blocked')
        else:
            messages.error(request,'Invalid Username and Password')
            return redirect(user_login)
            
    return render(request,'userlogin.html')



def homepage(request):
    if request.user.is_authenticated:
        context = {
            'posts':posts
        }
        return render(request,'home.html',context)
    return redirect(user_login)

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(user_login)



def user_signup(request):
    if request.method == 'POST':
        form =RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(user_login)

    form = RegisterationForm()
    context = {
        'form':form
    }
    return render(request,'usersignup.html',context)


# def adminlogin(request):
#     return render(request,'adminlogin.html')



       # username = request.POST['username']
        # email = request.POST['email']
        # password = request.POST['password']
        # confirm_password = request.POST['confirm_password']
        # password_encrypt = sha256(password.encode()).hexdigest()

        # if password == confirm_password:
        #     if User.objects.filter(username=username).exists():
        #         messages.info(request,'Username Exists')
        #         return redirect(user_signup)
        #     else:
        #         User(username = username, password = password_encrypt, email = email).save()
        #         return redirect(user_login)
        # else:
        #     messages.error(request,'Password not match..')
        #     return redirect(user_signup)





# def formlogin(request):
#     form = CreateUserForm()
#     return render(request,'index.html',{'form':form})
