from django.shortcuts import render
from django.http import HttpResponse
from news.models import News, Comment
from django.views.generic import ListView, CreateView, DetailView
from django.forms import Form, ModelForm, widgets
from django.shortcuts import render_to_response


# Create your views here.
class AddNewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'news': widgets.HiddenInput
        }


class NewsListView(ListView):
    model = News
    template_name = 'list_news.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        queryset = News.objects.order_by('-added_date')
        return queryset



class NewsDetailView(DetailView):
    model = News
    template_name = 'detail_news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(news=self.object)
        context['form'] = AddCommentForm(initial={'news': self.object.pk})
        return context


class NewsCreateView(CreateView):
    model = News
    template_name = 'add_news.html'
    form_class = AddNewsForm


class CommentCreateView(CreateView):
    model = Comment
    form_class = AddCommentForm
    http_method_names = ['post']
    template_name = 'add_comment.html'




