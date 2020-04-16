from django.urls import path
from ebooks.api.views import EbookListCreateView

urlpatterns = [
    path("ebooks/", EbookListCreateView.as_view(), name="ebook-list")
]
