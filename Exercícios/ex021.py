# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.
import pygame

pygame.mixer.init()
pygame.mixer.music.load('tomp3.cc - GigaChad Theme Phonk House Version.mp4')
pygame.mixer.music.play()
input()
pygame.event.wait()
