import pygame
import sys

LARGURA = 600
ALTURA = 600
TAMANHO_CELULA = 200

BRANCO = (255,255,255)
PRETO = (0,0,0)
VERMELHO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0, 255, 0)

tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Matriz Visual com pygame")


executando = True
while executando:
    #verificar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    
    #Preenche a tela com a cor branca
    tela.fill(BRANCO)
    
    #Atualiza a tela
    pygame.display.flip()
    
#Encerra o jogo
pygame.quit()
sys.exit()