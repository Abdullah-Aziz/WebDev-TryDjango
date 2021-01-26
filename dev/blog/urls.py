from django.urls import path
from dev.blog.views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articles-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='articles-detail'),  # id == pk
    path('create/', ArticleCreateView.as_view(), name='articles-create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='articles-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='articles-delete'),
]
