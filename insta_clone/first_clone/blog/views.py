from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (TemplateView,ListView,
                                DetailView,CreateView,DeleteView,
                                UpdateView)
from blog.models import Post,Comment,Signup
from django.contrib.auth.models import User
from blog.forms import PostForm,CommentForm,SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import  LoginRequiredMixin 
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'

@login_required
def UserInfo(request,id):
       # user=User.objects.get(id=id)
        User_detail=Signup.objects.get(id=id)
        user_details=User.objects.get(id=User_detail.id)  
        post=Post.objects.filter(author_id=User_detail.id).count()
        context={
            'person': User_detail,
            'user':user_details,
            'post':post
        }
        return render(request, 'registrations/profile.html',context)


class SignupView(CreateView):
    model = Signup
    form_class =SignupForm
    success_url=reverse_lazy('login')
    template_name='registrations/signup.html'




class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    #login_url='/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class =PostForm
    model = Post
    
    

class PostUpdateView(LoginRequiredMixin,UpdateView):
     login_url='/login/'
     redirect_field_name = 'blog/post_detail.html'
     form_class =PostForm
     model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name='blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')



##############################################
##############################################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

@login_required
def add_comment_to_publish(request,pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post =post
            comment.save()
            return redirect('post_detail',pk=pk)
    
    else:
        form=CommentForm()
    return render(request,'blog/comment_form.html', {'form': form})

@login_required
def comment_approve(request,pk):
    new_comment=get_object_or_404(Comment,pk=pk)
    new_comment.approve()
    return redirect('post_detail',pk=new_comment.post.pk)


@login_required
def comment_remove(request,pk):
   new_comment=get_object_or_404(Comment,pk=pk)
   post_pk=new_comment.post.pk
   new_comment.delete()
   return redirect('post_detail',pk=post_pk)


