from users.deocrators import allowed_users
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import RegisterForm,ProfileForm
from .models import Profile
from django.contrib.auth.models import Group, User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_text

from django.http import HttpResponse
# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active= False
            user.save()
            group= Group.objects.get(name='Customer')
            user.groups.add(group)
            sent_app_email(request,user)
            username= form.cleaned_data.get('username')
            messages.success(request,f'Welocme {username},account created successfully')
            return redirect('login')
    else:
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form})

def sent_app_email(request,user):
    current_site = get_current_site(request)
    email_subject= 'Registration Varification Mail'

    message = render_to_string('email_template.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token': account_activation_token.make_token(user),
                        })
    send_mail(
                email_subject,
                message,
                'shezan.new@gmail.com',
                [user.email],
                fail_silently=False,
            )

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        username= user.username
        messages.success(request,f'Congrtulation {username},Account has been Varified Succesfully, You Can Login Now')
    return redirect('login')

def profile(request):
    
    if(Profile.objects.filter(user=request.user.id).exists()):
        profile=Profile.objects.get(user=request.user.id)
        if request.method=='POST':
            form=ProfileForm(request.POST,request.FILES,instance=profile)
            form.fields["user"].queryset = User.objects.filter(id=request.user.id)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('user')
                messages.success(request,f'Hi {user},Profile Updated Successfully')
                return redirect('index')

        else:
            form=ProfileForm(request.POST or None,instance=profile)
            form.fields["user"].queryset = User.objects.filter(id=request.user.id)
            return render(request,'users/profile_create.html',{'form':form})
    else:
        if request.method=='POST':
            form=ProfileForm(request.POST,request.FILES)
            form.fields["user"].queryset = User.objects.filter(id=request.user.id)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('user')
                messages.success(request,f'Hi {user},Profile Updated Successfully')
                return redirect('index')
        else:
            form=ProfileForm()
            form.fields["user"].queryset = User.objects.filter(id=request.user.id)
        return render(request,'users/profile_create.html',{'form':form})
@allowed_users(allowed_roles=['Customer'])
def profileView(request):
    if(Profile.objects.filter(user=request.user.id).exists()):
        current_user= request.user.id
        #print (current_user)
        profile=Profile.objects.get(user=current_user)
    
        return render(request,'users/profile_view.html',{'profile':profile})
    else:
        if request.method=='POST':
            form=ProfileForm(request.POST,request.FILES)
            form.fields["user"].queryset = User.objects.filter(id=request.user.id)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('user')
                messages.success(request,f'Hi {user},Profile Updated Successfully')
                return redirect('index')
        else:
            form=ProfileForm()
            form.fields["user"].queryset = User.objects.filter(id=request.user.id)
        return render(request,'users/profile_create.html',{'form':form})

       
