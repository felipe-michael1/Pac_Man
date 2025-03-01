from pacman import pygame
from pacman import TAMANHO_BLOCO
from pacman import BRANCO
from pacman import VERMELHO
from pacman import ROSA
from pacman import CIANO
from pacman import LARANJA
from pacman import AMARELO
from pacman import LARGURA
# Define uma classe chamada 'Jogador'.
class Jogador:
    
    # Método construtor que é chamado quando uma nova instância da classe é criada.
    def __init__(self, x, y):
    
        # A posição inicial do jogador é armazenada como uma lista 
                # de duas coordenadas: x e y.
        self.posicao = [x, y]
        
        # A direção atual do movimento do jogador é armazenada como uma lista.
        # Inicialmente, está definido para [0, 0], o que significa que o 
                # jogador não está se movendo.
        self.direcao = [0, 0]
        
        # A direção desejada é a direção para a qual o jogador quer se mover.
        # Isso pode mudar com base nas entradas do usuário (por exemplo,
                # pressionar uma tecla de seta).
        self.direcao_desejada = [0, 0]
        
        # Define a velocidade do jogador, que neste caso é um valor constante de 2.
        # Isso pode ser ajustado para tornar o jogo mais fácil ou mais difícil.
        self.velocidade = 2
        
        # Cria um objeto retângulo que representa a posição e 
                # tamanho do jogador na tela.
        # 'pygame.Rect' é usado para criar um retângulo onde 'x' e 'y'
                # são as coordenadas iniciais,
                # e 'TAMANHO_BLOCO' é a largura e altura do retângulo.
        self.retangulo = pygame.Rect(x, y, TAMANHO_BLOCO, TAMANHO_BLOCO)

    
    def mover(self, paredes):
        
        # Verifica se a direção que o jogador deseja seguir é
                # diferente da direção atual.
        if self.direcao_desejada != self.direcao:
            
            # Calcula qual seria a nova posição se o jogador seguir na direção desejada.
            nova_posicao = [self.posicao[0] + self.direcao_desejada[0] * self.velocidade,
                            self.posicao[1] + self.direcao_desejada[1] * self.velocidade]
            
            # Cria um retângulo de colisão na nova posição para 
                    # testar interseção com paredes.
            novo_retangulo = pygame.Rect(nova_posicao[0], nova_posicao[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
            
            # Testa se o novo retângulo colide com alguma das paredes do jogo.
            if not self.verificar_colisao(novo_retangulo, paredes):
                
                # Atualiza a direção atual do jogador para a direção 
                        # desejada, pois não há colisão.
                self.direcao = self.direcao_desejada
    
        # Calcula a nova posição do jogador baseando-se na direção atual.
        nova_posicao = [self.posicao[0] + self.direcao[0] * self.velocidade,
                        self.posicao[1] + self.direcao[1] * self.velocidade]
        
        # Cria outro retângulo de colisão para a nova posição calculada.
        novo_retangulo = pygame.Rect(nova_posicao[0], nova_posicao[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
        
        # Verifica se o retângulo criado colide com qualquer parede.
        if not self.verificar_colisao(novo_retangulo, paredes):
            
            # Se não há colisão, atualiza a posição do jogador no jogo.
            self.posicao = nova_posicao
            
            # Atualiza o retângulo de colisão para a nova posição.
            self.retangulo = novo_retangulo
            
        else:
            
            # Se houver colisão, alinha o jogador ao bloco mais próximo 
                    # para evitar movimento parcial dentro das paredes.
            self.alinhar()
    
        # Verifica se o jogador atravessa os limites horizontais do
                # mapa para teletransporte.
        if self.posicao[0] < -TAMANHO_BLOCO:
            
            # Se o jogador sair pelo lado esquerdo, ele aparece no 
                    # lado direito da tela.
            self.posicao[0] = LARGURA
            
        elif self.posicao[0] > LARGURA:
            
            # Se o jogador sair pelo lado direito, ele aparece no
                    # lado esquerdo da tela.
            self.posicao[0] = -TAMANHO_BLOCO
    
        # Atualiza a posição do topo esquerdo do retângulo para
                # corresponder à nova posição do jogador.
        self.retangulo.topleft = self.posicao


    
    # Define o método 'verificar_colisao' na classe Jogador para
                # verificar colisões com as paredes.
    def verificar_colisao(self, retangulo, paredes):
        
        # Itera sobre a lista de paredes para verificar se há colisão 
                # entre o retângulo do jogador e qualquer parede.
        for parede in paredes:
            
            # Para cada parede na lista, verifica se o retângulo do 
                    # jogador intersecciona com a parede.
            if retangulo.colliderect(parede):
                
                # Se o retângulo do jogador intersecciona com alguma 
                        # das paredes, retorna True.
                return True
                
        # Se o loop terminar e nenhuma interseção for
                # detectada, retorna False.
        return False
    
    # Define o método 'alinhar' na classe Jogador para alinhar a
            # posição do jogador ao grid do labirinto.
    def alinhar(self):
        
        # Arredonda a posição x do jogador para o múltiplo mais
                # próximo de TAMANHO_BLOCO.
        self.posicao[0] = round(self.posicao[0] / TAMANHO_BLOCO) * TAMANHO_BLOCO
        
        # Arredonda a posição y do jogador para o múltiplo mais
                # próximo de TAMANHO_BLOCO.
        self.posicao[1] = round(self.posicao[1] / TAMANHO_BLOCO) * TAMANHO_BLOCO
        
        # Atualiza a posição do retângulo de colisão do jogador 
                # para refletir o alinhamento.
        self.retangulo.topleft = self.posicao


    # Método responsável por desenhar o jogador na superfície de jogo.
    def desenhar(self, superficie):
        
        # Desenha um círculo na superfície do jogo representando o jogador.
        # A cor do círculo é definida como AMARELO, e a posição é 
                # centralizada no bloco onde o jogador está.
        pygame.draw.circle(superficie, AMARELO, (int(self.posicao[0]) + TAMANHO_BLOCO // 2, int(self.posicao[1]) + TAMANHO_BLOCO // 2), TAMANHO_BLOCO // 2)
        
    # Método que permite ao jogador coletar pontos no jogo.
    def comer_ponto(self, pontos):
        
        # Itera sobre uma cópia da lista de pontos para permitir 
                # modificação durante a iteração.
        for ponto in pontos[:]:
            
            # Verifica se o retângulo do jogador colide com o 
                    # retângulo de um ponto.
            if self.retangulo.colliderect(ponto.retangulo):
                
                # Se colidir, o ponto é removido da lista de pontos.
                pontos.remove(ponto)
                
                # Retorna 1 para indicar que um ponto foi ganho.
                return 1
                
        # Se não houver colisão com nenhum ponto, retorna 0.
        return 0
    
    # Método que permite ao jogador coletar pastilhas no jogo.
    def comer_pastilha(self, pastilhas):
        
        # Itera sobre uma cópia da lista de pastilhas para 
                # permitir modificação durante a iteração.
        for pastilha in pastilhas[:]:
            
            # Verifica se o retângulo do jogador colide com o 
                    # retângulo de uma pastilha.
            if self.retangulo.colliderect(pastilha.retangulo):
                
                # Se colidir, a pastilha é removida da lista de pastilhas.
                pastilhas.remove(pastilha)
                
                # Retorna 50 para indicar que 50 pontos foram ganhos.
                return 50
                
        # Se não houver colisão com nenhuma pastilha, retorna 0.
        return 0






