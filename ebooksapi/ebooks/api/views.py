from rest_framework import generics
from rest_framework.generics import get_object_or_404
# from rest_framework import permissions
from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer
from ebooks.api.permissions import IsAdminUserOrReadOnly


#concret generic views
class EbookListCreateView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class EbookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# generic views using mixins
# class EbookListCreateView(mixins.ListModelMixin,
#                             mixins.CreateModelMixin,
#                             generics.GenericAPIView):
    
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(self, request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(self, request, *args, **kwargs)