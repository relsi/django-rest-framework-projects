from rest_framework import generics, mixins
from ebooks.models import Ebook
from ebooks.api.serializers import EbookSerializer

class EbookListCreateView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):
    
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(self, request, *args, **kwargs)