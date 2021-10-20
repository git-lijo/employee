from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class HomeView(ListView):
    model = EmployeeData
    template_name = "home.html"


class PostDetailView(DetailView):
    model = EmployeeData
    template_name = "post_detail.html"


class AddPostView(CreateView):
    model = EmployeeData
    form_class = PostForm
    template_name = "add_post.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        User.objects.create_user(username=obj.EmpName, email=obj.EmpMail, password=obj.Password)
        return super().form_valid(form)

