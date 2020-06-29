from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import File
from django.contrib.auth.models import User


def home(request):
  return render(request,'filebox/base.html',{'title':'FileShare'})

class UploadListView(LoginRequiredMixin,ListView):
    model=File
    template_name='filebox/home.html'
    context_object_name='posts'
    ordering=['-date_uploaded']
    paginate_by=5

class UserUploadListView(ListView):
    model=File
    template_name='filebox/user_posts.html'
    context_object_name='posts'
    paginate_by=4
    
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return File.objects.filter(uploaded_by=user).order_by('-date_uploaded')

class UploadDetailView(DetailView):
    model=File

class UploadCreateView(LoginRequiredMixin, CreateView):
    model=File
    fields=['about','file']
    def form_valid(self,form):
        form.instance.uploaded_by=self.request.user
        return super().form_valid(form)    

class UploadUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=File
    fields=['about','file']
    def form_valid(self,form):
        form.instance.uploaded_by=self.request.user
        return super().form_valid(form)    
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.uploaded_by:
            return True
        return False

class UploadDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=File
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.uploaded_by:
            return True
        return False

def about(request):
  return render(request,'filebox/about.html',{'title':'About'})

