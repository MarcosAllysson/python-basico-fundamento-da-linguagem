"""
Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.
"""
#Módulo de jogos do python que também pode ser usado pra reproduzir áudios
import pygame
import emoji

print(emoji.emojize('REPRODUZINDO ÁUDIO MP3 :musical_note: :fire: '))

#inicializando pygame
pygame.init()

#carrego o áudio que está na próprio diretório
pygame.mixer.music.load('ex021.mp3')

#dando play no áudio
pygame.mixer.music.play()

#esperando terminar até que o áudio acabe
pygame.event.wait()

