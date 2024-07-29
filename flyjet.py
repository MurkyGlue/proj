import pygame
import random

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))

hole = [random.randint(0, 1200), height/2-4]
holeSize = [4, 6]

hole2 = [random.randint(0, 1200), height/2-4]
holeSize2 = [4, 6]

char = [565, 550]
charSize = [150, 80]
wallSpeed = 0.3
charSpeed = 0


jetcol = (255, 0, 0)
wallcol = (0, 255, 0)
screencol = (100, 100, 100)

pygame.init()
while True:
	screen.fill(screencol)
	pygame.draw.rect(screen, wallcol, [hole, holeSize], 10)
	pygame.draw.rect(screen, jetcol, [char, charSize])
	
	pygame.display.flip()
	
	holeSize[0] += wallSpeed
	holeSize[1] += wallSpeed*(holeSize[1]/holeSize[0])
	hole[0] -= wallSpeed/2 + charSpeed
	hole[1] -= (wallSpeed*(holeSize[1]/holeSize[0]))/2
	wallSpeed += 0.0005
	
	
	if holeSize[1] > height+20:
		if hole[0] > width+20:
			hole = [random.randint(0, 1200), height/2-4]
			holeSize = [4, 6]
			wallSpeed = 0.3
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				charSpeed = 0.3
			if event.key == pygame.K_a:
				charSpeed = -0.3
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_d or event.key == pygame.K_a:
				charSpeed = 0

	
	
	
	
