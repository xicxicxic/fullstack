from django.db import models
from jogador.models import Jogador
from equipa.models import Equipa

# Create your models here.

class Jogo(models.Model):
    id = models.BigAutoField(primary_key=True)
    golos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jogo'
        
        
class Jogoequipa(models.Model):
    id_jogo = models.ForeignKey(Jogo, models.DO_NOTHING, db_column='id_jogo')
    id_equipa = models.ForeignKey(Equipa, models.DO_NOTHING, db_column='id_equipa')

    class Meta:
        managed = False
        db_table = 'jogoequipa'


class Jogojogador(models.Model):
    id_jogo = models.ForeignKey(Jogo, models.DO_NOTHING, db_column='id_jogo', blank=True, null=True)
    id_jogador = models.ForeignKey(Jogador, models.DO_NOTHING, db_column='id_jogador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jogojogador'
