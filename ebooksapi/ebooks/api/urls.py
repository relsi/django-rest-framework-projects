from django.urls import path
from ebooks.api.views import (EbookListCreateView, EbookDetailView, 
                              ReviewCreateView, ReviewDetailView)

urlpatterns = [
    path("ebooks/", EbookListCreateView.as_view(), name="ebook-list"),
    path("ebooks/<int:pk>/", EbookDetailView.as_view(), name="ebook-detail"),
    path("ebooks/<int:ebook_pk>/review/", ReviewCreateView.as_view(), name="ebook-review"),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review-detail")
]
