from rest_framework import serializers
from .models import Movie, Genre, Actor
from rest_framework.reverse import reverse


class MovieSerializer(serializers.ModelSerializer):
    genre_name = serializers.SerializerMethodField()
    cast_full_name = serializers.SerializerMethodField()
    absolute_url = serializers.SerializerMethodField()

    def get_genre_name(self, movie): 
        return movie.genre.name if movie.genre else None
    
    def get_cast_full_name(self, movie):
        return ActorSerializer(movie.cast.all(), many=True).data
    
    def get_absolute_url(self, movie):
        return  movie.get_absolute_url()
    
    class Meta:
        model = Movie 
        fields = "__all__"
        
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ["id","name"]
        
class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    
    def get_full_name(self, actor):
        return f"{actor.first_name} {actor.last_name}"
    
    
    
    class Meta:
        model = Actor 
        fields = "__all__"