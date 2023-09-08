from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse



# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *

# Create your views here.

#LIST MOVIE AND GENRE AND ACTOR



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'movies': reverse('movie-list', request=request, format=format),
        'actors': reverse('actor-list', request=request, format=format),
        'genres': reverse('genre-list', request=request, format=format)
    })




class MovieListView(APIView):
    def get(self, request):
        cast_id = request.query_params.get('cast_id')
        genre_name = request.GET.get('genre', "all")
        sort = request.GET.get('sort', "-starRating")
        
        movies = Movie.objects.all().order_by(sort)
                
        if cast_id:
            movies = movies.filter(cast__id=cast_id)  # Filter movies by cast member's ID
            serializer = MovieSerializer(movies, request, many=True)
                        
        if genre_name.lower() != "all" :
            movies = movies.filter(genre__name__iexact=genre_name)
            
        
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        errors = serializer.errors
        errors['custom_message'] = 'Custom error message чето нетак с сохронением'

        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
     
     
#GENRE
    
@api_view(['GET', 'POST'])
def genre_list(request):
    actor_id = request.query_params.get('actor_id')

    if request.method == 'GET':
        data = Genre.objects.all()
        
        if actor_id:
            data = Genre.objects.filter(movie__cast__id=actor_id).distinct()
                   
        serializer = GenreSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        print('post')
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# ACTOR    
 
@api_view(['GET', 'POST'])
def actor_list(request):
    if request.method == 'GET':
        data = Actor.objects.all()
        serializer = ActorSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print('post')
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
#DETAIL 
    
@api_view(['GET'])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie, context={'request': request})
    return Response(serializer.data)



class MovieDeleteView(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie, context={'request': request})
        return Response(serializer.data)
        
    def delete(self, request, pk):
        # Get the movie instance to be deleted or return 404 if it doesn't exist
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()  # Delete the movie
        return JsonResponse({'message': 'Movie deleted successfully'})



@api_view(['GET'])
def genre_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GenreSerializer(genre, context={'request': request})
    return Response(serializer.data)

class ActorDetailView(APIView):
    def get(self, request, actor_id):
        actor = Actor.objects.get(pk=actor_id)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)
    
    
    
#UPDATE

@api_view(['GET','PUT', 'DELETE'])
def movie_update(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie, context={'request': request})
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['GET','PUT', 'DELETE'])
def genre_update(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = GenreSerializer(genre, context={'request': request})
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = GenreSerializer(genre, data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
@api_view(['GET','PUT', 'DELETE'])
def actor_update(request, pk):
    try:
        actor = Actor.objects.get(pk=pk)
    except Actor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ActorSerializer(actor, context={'request': request})
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ActorSerializer(actor, data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    

    
