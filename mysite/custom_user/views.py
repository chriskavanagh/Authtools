from django.shortcuts import render, redirect
#from .forms import EmailUserCreateForm
from authtools.forms import UserCreationForm
#from django.contrib.auth.forms import AuthenticationForm
from .forms import UserLoginForm, EmailTestForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.sites.models import Site
from django.conf import settings
from django.template import loader



# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_done')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
        
        
def register_done(request):
    return render(request, 'register_done.html', {})

    
def login_view(request):
    #next = request.GET.get('next')
    form = UserLoginForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            
            if user is not None and user.is_active:
                login(request, user)
                return redirect('loggedin')
    else:
        form = UserLoginForm()
        return render(request, 'registration/login.html', {'form': form})
    
    
@login_required    
def logout_view(request):
    logout(request)
    return render(request, 'registration/loggedout.html')


def logged_in(request):
    return render(request, 'registration/loggedin.html')


def send_email(request):
    User = get_user_model()
    if request.method == 'POST':
        form = EmailTestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            to_email = form.cleaned_data['email']   # cd['email']
            subject = 'email test'
            from_email = settings.EMAIL_HOST_USER
            domain = Site.objects.get_current().domain
            context = {
                      'uuid64': urlsafe_base64_encode(force_bytes(user.pk)),
                      'token': default_token_generator.make_token(user),
                      'user': user,
                      'domain':domain,
                      }
            email = loader.render_to_string('email_text.html', context)
            send_mail(subject, email, from_email, [to_email], fail_silently=False)
            return redirect('login')
    else:
        form = EmailTestForm()
        context = {'form':form}
        return render(request, 'send_mail.html', context)        


def test_email_confirm(request, uuid64=None, token=None):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uuid64)
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, UserModel.DoesNotExist):
        user = None
        
    if user == None:
        return redirect('register')
    
    if user is not None and default_token_generator.check_token(user, token):
        return redirect('login')
    
    
    
            
    
    
    
# def register(request):
    # if request.method == 'POST':
        # user_form = UserRegistrationForm(request.POST)

        # if user_form.is_valid():
            # # Create a new user object but avoid saving it yet
            # new_user = user_form.save(commit=False)
            # # Set the chosen password
            # new_user.set_password(user_form.cleaned_data['password'])
            # # Save the User object
            # new_user.save()
            # # Create the user profile
            # profile = Profile.objects.create(user=new_user)
            # return render(request,
                          # 'account/register_done.html',
                          # {'new_user': new_user})
    # else:
        # user_form = UserRegistrationForm()
    # return render(request, 'account/register.html', {'user_form': user_form})
    
    