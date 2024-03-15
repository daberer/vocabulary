from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WordsSerializer
from .models import Words
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.http import HttpResponse
from django.db.models import Count

# Create your views here.
@api_view(['GET', 'POST'])
def word_list(request, format=None):
     if request.method == 'GET':
          words = Words.objects.all()
          serializer = WordsSerializer(words, many=True)
          return Response(serializer.data)
     if request.method == 'POST':
          serializer = WordsSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def word_list_box(request, id, format=None):
     if request.method == 'GET':
          words = Words.objects.filter(box=id)
          serializer = WordsSerializer(words, many=True)
          return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def word_detail(request, id, format=None):
     try:
          word = Words.objects.get(pk=id)
     except Words.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)
     if request.method == 'GET':
          serializer = WordsSerializer(word)
          return Response(serializer.data)
     if request.method == 'PUT':
          serializer = WordsSerializer(word, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     if request.method == 'DELETE':
          word.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def random_word(request):
     random_word = Words.objects.order_by('?').first()
     serializer = WordsSerializer(random_word)
     return Response(serializer.data)

def get_number_for_each_box(request):
     p = Words.objects.values('box').annotate(dcount=Count('box')).order_by()
     return JsonResponse({x['box']:x['dcount'] for x in p}, safe=False)

def read_from_csv(request):
     df = pd.read_csv('../some_words.csv')
     for i, row in df.iterrows():
          word = Words(english=row.english, spanish=row.spanish, info=row['info'], box=0)
          word.save()
     return HttpResponse('Words saved successfully!')
