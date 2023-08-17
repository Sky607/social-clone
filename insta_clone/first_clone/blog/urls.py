from django.urls import re_path,path
from django.contrib.auth.views import LoginView,LogoutView
from blog import views



urlpatterns =[
    re_path(r'^$',views.PostListView.as_view(),name='post_list'),
    re_path(r'signup/$',views.SignupView.as_view(),name='signup'),
    re_path(r'^about/$',views.AboutView.as_view(),name='about'),
    re_path(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    re_path(r'^post/new/$',views.PostCreateView.as_view(),name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_update'),
    re_path(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_delete'),
    re_path(r'^drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_publish,name='add_comment_to_publish'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    re_path(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),

    re_path(r'accounts/login/$',LoginView.as_view(template_name='registrations/login.html'),name='login'),
    re_path(r'accounts/logout/$',LogoutView.as_view(template_name='blog/post_list.html'),name='logout'),
    path('accounts/userinfo/<int:id>',views.UserInfo,name='userinfo'),
    path('accounts/profile/',views.PostListView.as_view(),name='profile')

]