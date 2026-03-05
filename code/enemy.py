#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

class Enemy:
    def __init__(self,name,position,frame_path):
        self.name = name
        self.x,self.y = position
        self.frames = self.load_frames(frame_path)
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect(topleft=(self.x,self.y))
        self.speed = 5

    def load_frames(self,frame_path):
        frames = []
        for frame in frame_path:
            frames.append(pygame.image.load(frame).convert_alpha())
        return frames

    def move(self):
        #movimento horizontal simples
        self.x -= self.speed
        self.rect.topleft = (self.x,self.y)
        #animação simples
        self.frame_atual += 0.2
        if self.frame_atual >= len(self.frames):
            self.frame_atual = 0
        self.image = self.frames[int(self.frame_atual)]


    def draw(self,window):
        window.blit(self.image,(self.x,self.y))
        pass
