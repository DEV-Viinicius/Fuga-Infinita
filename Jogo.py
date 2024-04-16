import pygame
from pygame.locals import * 
from  sys import  exit
from random import randint

pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2

x_azul = randint(40,600)
y_azul = randint(50,430)
fonte = pygame.font.SysFont('ARIAL',40,True,True)

tela = pygame.display.set_mode((largura , altura ))
pygame.display.set_caption('JOGO')
relegio = pygame.time.Clock()
pontos=0

while True:
    relegio.tick(20)
    tela.fill((0,0,0))
    mesagem= f'Pontos:{pontos}'
    texto_formatado = fonte.render(mesagem,True,(255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x=x + 20 
    if pygame.key.get_pressed()[K_s]:
        y=y + 20
    if pygame.key.get_pressed()[K_w]:
        y=y - 20

    ret_vermnelho =pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50))

    borta = pygame.draw.rect(tela,(0,255,0),pygame.Rect(0,0,640,480),10)

    ret_azul = pygame.draw.rect(tela, (255,0,0), (x,y,40,50))

    
    if ret_vermnelho.colliderect(ret_azul):
        x_azul = randint(40,600)
        y_azul = randint(50,430)
        pontos=pontos+1

    if x < 0 or x > largura - 40 or y < 0 or y > altura - 50:
        mensagem_sair_tela = "Você saiu da tela!"
        texto_sair_tela = fonte.render(mensagem_sair_tela, True, (255, 255, 255))
        tela.blit(texto_sair_tela, (largura / 2 - 150, altura / 2))
        pontos= 0 

    


    tela.blit(texto_formatado,(450,40))
    pygame.display.update()