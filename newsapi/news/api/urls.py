from django.urls import path
from news.api.views import article_api_view

urlpatterns = [
    path("articles/", article_api_view, name="article-list")
]