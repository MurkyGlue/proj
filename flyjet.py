import pygame
import random

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))

hole = [random.randint(0, 1200), height/2-4]
holeSize = [4, 6]

hole2 = [random.randint(0, 1200), height/2-4]
holeSize2 = [6, 6]

char = [565, 550]
charSize = [150, 80]
wallSpeed = 0.2
charSpeed = 0
wallSpeed2 = 0.2

jetcol = (255, 0, 0)
wallcol = (0, 255, 0)
screencol = (100, 100, 100)

move = False

def move1():
	global holeSize, wallSpeed, hole
	holeSize[0] += wallSpeed
	holeSize[1] += wallSpeed*(holeSize[1]/holeSize[0])
	hole[0] -= wallSpeed/2 + charSpeed
	hole[1] -= (wallSpeed*(holeSize[1]/holeSize[0]))/2
	wallSpeed += 0.0005
	if holeSize[0] > width+20:
		hole = [random.randint(0, 1200), height/2-4]
		holeSize = [4, 6]
		wallSpeed = 0.2
	elif holeSize[1] > height+20:
		if not hole[0] < char[0] < char[0]+charSize[0] < hole[0]+holeSize[0]:
			print('end')
		
def move2():
	global holeSize2, wallSpeed2, hole2
	holeSize2[0] += wallSpeed2
	holeSize2[1] += wallSpeed2*(holeSize2[1]/holeSize2[0])
	hole2[0] -= wallSpeed2/2 + charSpeed
	hole2[1] -= (wallSpeed2*(holeSize2[1]/holeSize2[0]))/2
	wallSpeed2 += 0.0005
	if holeSize2[0] > width+20:
		hole2 = [random.randint(0, 1200), height/2-4]
		holeSize2 = [4, 6]
		wallSpeed2 = 0.2
	elif holeSize2[1] > height+20:
		if not hole2[0] < char[0] < char[0]+charSize[0] < hole2[0]+holeSize2[0]:
			print('end')

pygame.init()
while True:
	screen.fill(screencol)
	pygame.draw.rect(screen, wallcol, [hole, holeSize], 10)
	pygame.draw.rect(screen, wallcol, [hole2, holeSize2], 10)
	pygame.draw.rect(screen, jetcol, [char, charSize])
	
	pygame.display.flip()
	
	move1()
	move2()

	
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

	
	
	
	
