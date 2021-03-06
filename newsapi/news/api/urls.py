from django.urls import path
# from news.api.views import article_api_view, article_detail_api_view
from news.api.views import ArticleAPIView, ArticleDetailView, JournalistAPIView

urlpatterns = [
    path("articles/", ArticleAPIView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("journalists/", JournalistAPIView.as_view(), name="journalist-detail")
    # path("articles/", article_api_view, name="article-list"),
    # path("articles/<int:pk>/", article_detail_api_view, name="article-detail")
]