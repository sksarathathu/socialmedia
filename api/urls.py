from django.urls import path
from api import views

urlpatterns=[
    path("post/add",views.PostCreateView.as_view(),name="post-create"),
    path("index",views.IndexView.as_view(),name="home"),
    path("register",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("logout",views.SignOutView,name="signout")
]