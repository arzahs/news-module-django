from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.NewsListView.as_view(), name='list_news'),
    url(r'test/$', views.test),
    url(r'add/$', views.NewsCreateView.as_view(), name='add_news'),
    url(r'comment/add', views.CommentCreateView.as_view(), name='add_comment'),
    url(r'^(?P<pk>\d+)/$', views.NewsDetailView.as_view(), name='detail_news'),
]