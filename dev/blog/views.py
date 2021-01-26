from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse
from .forms import ArticleModelForm
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    DetailView
)

from .models import Article


# Create your views here.

class ArticleDeleteView(DeleteView):
    template_name = 'articles/articles_delete.html'

    def get_object(self):
        id_ = self.kwargs.get('id')  # kwargs being passed by url
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:articles-list')


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')  # kwargs being passed by url
        return get_object_or_404(Article, id=id_)
