from django.db import models
from jogador.models import Jogador
# Create your models here.

class Equipa(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'equipa'


class Jogadorequipa(models.Model):
    id_jogador = models.ForeignKey(Jogador, models.DO_NOTHING, db_column='id_jogador')
    id_equipa = models.ForeignKey(Equipa, models.DO_NOTHING, db_column='id_equipa')

    class Meta:
        managed = False
        db_table = 'jogadorequipa'

