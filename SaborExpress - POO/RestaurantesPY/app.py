from restaurante import Restaurante
from rich import print, inspect

boteco_balburdia = Restaurante('Blaburdia', 'Boteco')
restaurante_madalena = Restaurante('Madalena', 'Italiano')
boteco_balburdia.alternarEstado()
boteco_balburdia.receber_avaliacao("Joelson", 10)
boteco_balburdia.receber_avaliacao("Mauricio Bahia", 8)
boteco_balburdia.receber_avaliacao("Xaveco", 5)


def main():
    Restaurante.listar_restaurantes()
    

if __name__ == '__main__':
    main()