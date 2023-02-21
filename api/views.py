from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView

from api.forms import PostForm,CommentForm,RegistrationForm,LoginForm

from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login!!")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("signin")
    def form_valid(self, form):
        messages.success(self.request,"registration successful!!!")
        return super().form_valid(form)

class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})


@method_decorator(signin_required,name="dispatch")
class IndexView(TemplateView):
    template_name="index.html"

@method_decorator(signin_required,name="dispatch")
class PostCreateView(CreateView):
        template_name="post-add.html"
        form_class=PostForm


class CommentCreateView(CreateView):
        template_name="comment-add.html"
        form_class=CommentForm

@method_decorator(signin_required,name="dispatch")   
class PostDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        Posts.objects.get(id=id).delete()
        messages.success(request,"post has been removed")
        return redirect("home")

def SignOutView(request,*args,**kwargs):
    logout(request)
    return redirect("signin")
