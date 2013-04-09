import sys, pygame
import socket
from tabuleiro import *
import constantes
import configuration
import pickle as serialize

class GameServer(object):
    """
    """
    def __init__(self, tamanhoTab, nCasas ):
        """
        """
        self.tabuleiro = Tabuleiro(tamanhoTab, nCasas)
        self.estabeleceServer()
        self.jogo()

    def estabeleceServer(self):
        self.servidor = socket.socket()
        # nome da maquina local
        self.host = socket.gethostname()
        self.porta = configuration.porta
        self.servidor.bind((self.host, self.porta))
        self.servidor.listen(2) # numero maximo de conexoes

        self.jogadores = []
        self.jogadores.append(self.servidor.accept())
        self.jogadores.append(self.servidor.accept())

        self.servidor.setblocking(1)
        self.servidor.settimeout(0.1)

        self.jogoEmAndamento = True
        self.jogadorAtual = -1

    def getPorta(self):
      return self.porta

    def getJogoEmAndamento(self):
        return self.jogoEmAndamento
    
    def setJogoEmAndamento(self, valor):
        self.jogoEmAndamento = valor

    def jogo(self):
        print "vaicomercar"
        while self.getJogoEmAndamento():
            print "pipipipipipi"
            jogador = self.proximo_jogador()

            try:
                jogada = jogador[0].recv(1024)
                print jogada
                self.rodada(jogador, serialize.loads(jogada))
            finally:
                pass

    def rodada(self, jogador, jogada):
        """
        Arguments:
        - `jogador`:
        - `jogada`:
        """
        print jogada
        if (jogada == "FIM"):
            self.setJogoEmAndamento(False)
            #TODO: Fazer algo pro fim do jogo
        else:
            try:
                data = serialize.dumps({"mimimimimi", "uaaaaaaaaaaaaaa"})
                self.jogadores[0][0].sendall(data)
                self.jogadores[1][0].sendall(data)
            finally:
                self.servidor.close()



    def proximo_jogador(self):
        indice_jogador = (self.jogadorAtual + 1) % 2
        return self.jogadores[indice_jogador]

    def jogada(self, posicaoClique, jogador):
        """
        """
        casa = self.mapeia_casa(posicaoClique)
        if jogador == 0:
            self.desenha_jogador(casa, constantes.azul)
        else:
            self.desenha_jogador(casa, constantes.vermelho)
        self.tabuleiro.set_casa(casa, 1)
        self.tabuleiro.exibe()

gomoku = GameServer(configuration.tamanhoJanela, configuration.numCasas)


# casa vazia
# ao pressionar o botao muda de jogador
