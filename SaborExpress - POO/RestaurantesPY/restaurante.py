from rich import print, inspect
from avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria}| {restaurante.media_avaliacoes} | {restaurante.checar}")
    
    @property
    def checar(self):
        return "☒" if self._ativo else "☐"
    
    def alternarEstado(self):
        self._ativo = not self._ativo
        return self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quant_avaliacoes = len(self._avaliacao)
        media = round(soma_das_notas / quant_avaliacoes, 1)
        
        return media