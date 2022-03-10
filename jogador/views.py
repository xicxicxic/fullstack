from mailbox import NotEmptyError
from multiprocessing import allow_connection_pickling
from django.shortcuts import render
from django.http import HttpResponse
from jogador.models import Jogador,JogadorSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import ListAPIView
import json

# Create your views here.
@api_view(["POST"])
def getJogador(request,idJ,*args, **kwargs):
    jogadorQuery = Jogador.objects
    try:
        jogador = jogadorQuery.get(id=idJ)
        serializer = JogadorSerializer(jogador)  
        return Response(status=status.HTTP_200_OK,data={"data":serializer.data})
    except:
        print("Erro")
        return Response(status=status.HTTP_400_BAD_REQUEST,data={"Erro":"Esse id não existe!"})

@api_view(["POST"])
def allJogador(request,*args, **kwargs):
    allObjects = Jogador.objects.all()
    serializer = JogadorSerializer(allObjects,many=True)
    print(serializer.data)
    return Response(status=status.HTTP_200_OK,data=serializer.data)

    