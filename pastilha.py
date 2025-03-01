from pacman import pygame
from pacman import TAMANHO_BLOCO
from pacman import BRANCO

# Define a classe 'Pastilha', que representa as pastilhas 
            # energéticas maiores que o jogador pode coletar no jogo.
class Pastilha:
    
    # Método construtor que inicializa uma nova pastilha com coordenadas x e y.
    def __init__(self, x, y):
    
        # Armazena a posição da pastilha como uma lista de
                # duas coordenadas [x, y].
        self.posicao = [x, y]
        
        # Cria um retângulo de colisão para a pastilha. 
        # Este retângulo é posicionado no centro do bloco
        # com um deslocamento para centralizar um círculo 
                # de 8 pixels de diâmetro (4 pixels de raio).
        self.retangulo = pygame.Rect(x + TAMANHO_BLOCO//2 - 4, y + TAMANHO_BLOCO//2 - 4, 8, 8)
    
    # Método para desenhar a pastilha na superfície de jogo especificada.
    def desenhar(self, superficie):
        
        # Desenha um círculo branco na superfície de jogo que
                # representa a pastilha visualmente.
        # O círculo é desenhado no centro do bloco em que a 
                # pastilha está posicionada, sendo maior que os pontos comuns.
        pygame.draw.circle(superficie, BRANCO, (self.posicao[0] + TAMANHO_BLOCO // 2, self.posicao[1] + TAMANHO_BLOCO // 2), 4)


