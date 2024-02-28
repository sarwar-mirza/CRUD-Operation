from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, DetailView
from .forms import SignUpForm, LoginAuthenticationForm, ChangePasswordForm, ImageUploaderForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Picture

# Create your class based views here.
class HomeTemplateView(TemplateView):
    template_name = 'enroll/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Picture.objects.all()
        context = {'products': products}
        return context
    



# Create sign up function based views here
def signUp(request):
    # check this type (GET, POST)
    if request.method == 'POST':            # if statement for POST request
        fm = SignUpForm(request.POST)
        
        if fm.is_valid():       
            fm.save()
            messages.success(request, 'Congratulations!! Your account has been created successfully done')
            fm = SignUpForm()
    else:
        fm = SignUpForm()       # else statement for GET request
    return render(request, 'enroll/signup.html', {'form':fm})



# Create Login function based views
def login_user(request):
    if not request.user.is_authenticated:   # You can use to check if the user is authenticated otherwise stay here.
        if request.method == 'POST':
            fm = LoginAuthenticationForm(request=request, data= request.POST)
            
            if fm.is_valid():
                un = fm.cleaned_data['username']
                pw = fm.cleaned_data['password']

                user = authenticate(username=un, password=pw)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/accounts/dashboard/')
        
        else:
            fm = LoginAuthenticationForm(request=request)
        return render(request, 'enroll/login.html', {'form':fm})
    
    else:
        return HttpResponseRedirect('/accounts/dashboard/')


# Create Dashboard
def dashboard(request):
    if request.user.is_authenticated:   # User Confirm that the view can only be accessed by authenticated users.
        images = Picture.objects.all()    # database connected
        return render(request, 'enroll/dashboard.html', {'images': images})
    
    else:
        return HttpResponseRedirect('/accounts/login/')


# Create Logout
def logout_user(request):
    if request.user.is_authenticated:   # User Confirm that the view can only be accessed by authenticated users.
        logout(request)
        return HttpResponseRedirect('/accounts/login/')
    
    else:
        return HttpResponseRedirect('/accounts/login/')


# Create Change Password
def change_password(request):
    if request.user.is_authenticated:   # User Confirm that the view can only be accessed by authenticated users.
        if request.method == 'POST':
            fm = ChangePasswordForm(user=request.user, data=request.POST)
            
            if fm.is_valid():
                fm.save()
                
                messages.success(request, 'Congratulations!! Password change successfully done.')
        else:
            fm = ChangePasswordForm(user=request.user)
        return render(request, 'enroll/changepassword.html', {'form':fm})
    
    else:
        return HttpResponseRedirect('/accounts/login/')


# Add Operation
def add_img_upload(request):
    if request.user.is_authenticated:       # User Confirm that the view can only be accessed by authenticated users
        if request.method == 'POST':
            fm = ImageUploaderForm(request.POST, request.FILES)
            
            if fm.is_valid():
                fm.save()
                fm = ImageUploaderForm()
                messages.success(request, 'Image uploaded!!!')
        else:
            fm = ImageUploaderForm()
        return render(request, 'enroll/imgupload.html', {'form':fm})
    else:
        return HttpResponseRedirect('/accounts/login/')


# Update Operation
def update_info(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Picture.objects.get(pk=id)
            fm = ImageUploaderForm(request.POST, instance=pi)
            
            if fm.is_valid():
                fm.save()
                messages.info(request, 'Your data is Updated!!')
        else:
            pi = Picture.objects.get(pk=id)
            fm = ImageUploaderForm(instance=pi)
        return render(request, 'enroll/update.html', {'form':fm})
    
    else:
        return HttpResponseRedirect('/accounts/dashboard/')

# Delete product 
class DeleteRedirectView(RedirectView):
    url = '/accounts/dashboard/'
    
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Picture.objects.get(id=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)



# Product Details
class DetailProductDetailView(DetailView):
    model = Picture
    template_name = 'enroll/details.html'
    context_object_name = 'details'
    