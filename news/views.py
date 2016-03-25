from django.shortcuts import render
from django.http import HttpResponse
from news.models import News, Comment
from django.views.generic import ListView, CreateView, DetailView
from django.forms import Form, ModelForm, widgets
from django.shortcuts import render_to_response

# Create your views here.
def test(request):
    return HttpResponse('OK', status=200)

def test2(request, pk, *args, **kwargs):
    return HttpResponse('OK2', status=200)


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


class NewsDetailView(DetailView):
    model = News
    template_name = 'detail_news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.order_by('-added_date')
        context['form'] = AddCommentForm(initial={'news': self.object.pk})
        return context

    # def post(self, request, *args, **kwargs):
    #     form = AddCommentForm(request.POST)
    #     return self.render_to_response(self.get_context_data())


class NewsCreateView(CreateView):
    model = News
    template_name = 'add_news.html'
    form_class = AddNewsForm


class CommentCreateView(CreateView):
    model = Comment
    form_class = AddCommentForm
    http_method_names = ['post']




