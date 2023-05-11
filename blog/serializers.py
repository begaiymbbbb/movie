from django.db.models import Count
from rest_framework import serializers, generics
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count')

    def get_movies_count(self, obj):
        return obj.movie_set.count()


class DirectorList(generics.ListAPIView):
    queryset = Director.objects.annotate(movies_count=Count('movie'))
    serializer_class = DirectorSerializer


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'stars')


class MovieSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'reviews')

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        return ReviewSerializer(reviews, many=True).data


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'reviews', 'avg_rating')

    def get_avg_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.count() > 0:
            return sum(review.stars for review in reviews) / reviews.count()
        else:
            return 0