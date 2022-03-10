from dataclasses import fields
from django.db import models
from rest_framework import serializers

# Create your models here.

class Jogador(models.Model):
    primeiro_nome = models.TextField(max_length=200)
    ultimo_nome = models.TextField(max_length=200,blank=True)
    alcunha = models.TextField(max_length=200,blank=True)
    golos = models.BigIntegerField(blank=True)
    assistencias = models.BigIntegerField(blank=True)
    
    class Meta:
        managed=False
        db_table='jogador'

# class JogadorSerializer(serializers.Serializer):
#     primeiro_nome = serializers.CharField()
#     ultimo_nome = serializers.CharField()
#     alcunha = serializers.CharField()
#     golos = serializers.IntegerField()
#     assistencias = serializers.IntegerField()
    
#     def create(self, validated_data):
#         return Jogador.objects.create(validated_data)

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'