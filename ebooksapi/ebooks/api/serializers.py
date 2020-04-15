from rest_framework import serializers
from ebooks.models import Ebook, Review


class ReviewSerializer(object):
    
    class Meta:
        model: Review
        fields: "__all__"

class EbookSerializer(object):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model: Ebook
        fields: "__all__"

