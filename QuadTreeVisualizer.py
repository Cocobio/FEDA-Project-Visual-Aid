##########################################################################################################################
#
# Generated by Ignacio Osorio
#
# Using pygames as GUI
#
# Backtracking algorithm implemented
# algorithm reference: https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker
#
# Randomized Kruskal algorithm implemented
# algorithm reference: https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Kruskal's_algorithm
# 
# solution: .............................
#
##########################################################################################################################


import pygame
import numpy as np
from QuadTree import QuadTree

background = (54,54,54)

# Screen size
width = 360*3
height = 180*3

pygame.init()

# Create screen, set title and icon
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quadtree")

running = True

q = QuadTree(360.0*3,3*180.0)

manual_insert = True

while running:
	# timer
	# pygame.time.wait(2)
	
	# event attender
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			p = [i for i in pygame.mouse.get_pos()]

			if manual_insert:
				q.add_point(*p)

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_b:
				q.toggle_boundingbox()
			elif event.key == pygame.K_l:
				manual_insert = not manual_insert
				q.manual_insert(manual_insert)


	# OpenGL Stuff
	screen.fill(background)

	q.draw(screen)

	pygame.display.update()

