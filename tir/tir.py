import pygame
import random
import time

pygame.font.init()

screen = pygame.display.set_mode((1280, 720))
start = pygame.image.load("start.png")
diffi = pygame.image.load("difficulty.png")
exit = pygame.image.load("exit.png")
easy = pygame.image.load("easy.png")
medium = pygame.image.load("medium.png")
hard = pygame.image.load("hard.png")
backgr = pygame.image.load("фон 2.jpg")
coin = pygame.image.load("coin.png")
count = pygame.image.load("count.png")
enemy1E = pygame.image.load("nuck1E.png")
enemy2E = pygame.image.load("nuck2E.png")
enemy3E = pygame.image.load("nuck3E.png")
enemy1M = pygame.image.load("nuck1M.png")
enemy2M = pygame.image.load("nuck2M.png")
enemy3M = pygame.image.load("nuck3M.png")
enemy1H = pygame.image.load("nuck1H.png")
enemy2H = pygame.image.load("nuck2H.png")
enemy3H = pygame.image.load("nuck3H.png")
enemy = [enemy1E, enemy2E, enemy3E, enemy1M, enemy2M, enemy3M, enemy1H, enemy2H, enemy3H]
char = pygame.image.load("isaac.png")
shoot = pygame.image.load("shoot.png")
dead = pygame.image.load("dead.png")

startX = (1280-200)//2
startY = 240
diffiX = (1280-376)//2
diffiY = 360
exitX = (1280-144)//2
exitY = 480
easyX = (1280-211)//2
easyY = 240
mediumX = (1280-321)//2
mediumY = 360-(70-50)
hardX = (1280-203)//2
hardY = 480-(69-50)
countX = (1280-200)//2
countY = 600-(50-50)



col1 = 255, 255, 0

col3 = 0, 255, 255
col4 = 255, 0, 0
conColor = 0, 0, 0

charSize = 60
enemySize = 80
shootSize = 20
coinSize = coin.get_width()
markX = 510
markY = 265
enemySpeed = 0
charSpeed = 0.7
shootSpeed = 1.2

playing = False
menu = True
difscreen = False
boost = [False, False]

opt = 1
dif = 1
con = 1
timer = 0
j = 0
d = 0
b = 0
b2 = 2



scon = pygame.font.Font(None, 50)
kills = pygame.font.Font(None, 100)
boosts = pygame.font.Font(None, 100)
times = pygame.font.Font(None, 100)

pygame.init()
while menu:
	screen.blit(backgr, (0,0))
	
	screen.blit(start, (startX, startY))
	screen.blit(diffi, (diffiX, diffiY))
	screen.blit(exit, (exitX, exitY))
	
	pygame.draw.circle(screen, col4, [markX, markY], 25)
	pygame.display.flip()
	
		

	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			 
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN and opt < 3:
				opt += 1
				markY += 120
			if event.key == pygame.K_UP and opt > 1:
				opt -= 1
				markY -= 120	
				
			if opt == 1: markX = startX-35
			elif opt == 2: markX = diffiX-35
			elif opt == 3: markX = exitX-35	
				
			if event.key == pygame.K_RETURN:
				if opt == 1:
					enemyX = []
					enemyY = []
					charSpeedX = 0
					charSpeedY = 0	
					charX = 1280/2 - charSize//2
					charY = 720/2 - charSize//2 
					shootX = [charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2, charX+charSize//2-shootSize//2]
					shootY = [charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2, charY+charSize//2-shootSize//2]
					shootSpeedX = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					shootSpeedY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					check = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
					coinX = random.randint(0, 1280-coinSize)
					coinY = random.randint(0, 720-coinSize)
					for i in range(con): #заполнение массива врагов
						enemyX.append(random.randint(0, 1280-enemySize))
						enemyY.append(random.randint(0, 720-enemySize))
					
					starttime = time.time()
					boostcount = 0
					killcount = 0
					
					playing = True
					while playing:
						screen.blit(backgr, (0,0))
						screen.blit(coin, (coinX, coinY))
						
						#отрисовка
						for i in range(len(check)):
							screen.blit(shoot, (shootX[i]-5, shootY[i]-5))
						screen.blit(char, (charX-5, charY-5))
						for i in range(len(enemyX)):
							screen.blit(enemy[b], (enemyX[i]-5, enemyY[i]-5))
							b += 1
							if b > b2:
								b = b2-2
							
	
						pygame.display.flip()
	
						#ограничение поля
						if charX >= 1280-charSize:  
							charX = 1280-charSize-1
							charSpeedX = 0
						elif charX <= 0:
							charX = 1
							charSpeedX = 0 
						if charY >= 720-charSize: 
							charY = 720-charSize-1
							charSpeedY = 0
						elif charY <= 0:
							charY = 1
							charSpeedY = 0

						#движение врагов
						if dif != 1:
							for i in range(len(enemyX)):
								if enemyX[i] < charX:
									enemyX[i] += enemySpeed
								elif enemyX[i] > charX:
									enemyX[i] -= enemySpeed
								if enemyY[i] < charY:
									enemyY[i] += enemySpeed
								elif enemyY[i] > charY:
									enemyY[i] -= enemySpeed



						#возврат снарядов
						for i in range(len(check)):
							if shootX[i]>1280 or shootX[i]<-shootSize or shootY[i]>720 or shootY[i]<-shootSize:
								check[i] = True
								
						#попадания		
						for g in range(len(enemyX)):
							for i in range(len(check)):
								if enemyX[g]-shootSize <= shootX[i] < shootX[i]+shootSize <= enemyX[g]+enemySize+shootSize and enemyY[g]-shootSize <= shootY[i] < shootY[i]+shootSize <= enemyY[g]+enemySize+shootSize:
									enemyX[g] = random.randint(0, 1280-enemySize)
									enemyY[g] = random.randint(0, 720-enemySize)
									check[i] = True
									killcount += 1
									
									
						#снаряды у игрока
						for i in range(len(check)):
							if check[i]:
								shootX[i] = charX + charSize//2-shootSize//2
								shootY[i] = charY + charSize//2-shootSize//2
								shootSpeedX[i] = 0
								shootSpeedY[i] = 0

						#смерть
						for i in range(len(enemyX)):	
							if enemyX[i]-charSize <= charX < charX+charSize <= enemyX[i]+enemySize+charSize and enemyY[i]-charSize <= charY < charY+charSize <= enemyY[i]+enemySize+charSize:
								if d == 1:
									playing = False
									d = 0
									
									screen.blit(dead, (0, 0))
									screen.blit(times.render(str((time.time()-starttime)*1000//10/100), True, conColor), (700, 250))
									screen.blit(kills.render(str(killcount), True, conColor), (700, 380))
									screen.blit(boosts.render(str(boostcount), True, conColor), (700, 510))
									pygame.display.flip()
									time.sleep(3)
								d = 1
								
								
						#обновление монеты
						if coinX-charSize <= charX < charX+charSize <= coinX+coinSize+charSize and coinY-charSize <= charY < charY+charSize <= coinY+coinSize+charSize:
							boost[random.randint(0,1)] = True
							coinX = -100
							coinY = -100
							boostcount += 1
						elif boost[0]:
							charSpeed = 1.7
							shootSpeed = 2.2
							timer += 0.01
							if timer > 10:
								charSpeed = 0.7
								shootSpeed = 1.2
								timer = 0
								coinX = random.randint(0, 1280-coinSize)
								coinY = random.randint(0, 720-coinSize)
								boost[0] = False
						elif boost[1]:
							enemySpeed = 0
							timer += 0.01
							if timer > 10:
								if dif != 1:
									enemySpeed = 0.2 if dif == 2 else 0.5
								timer = 0
								coinX = random.randint(0, 1280-coinSize)
								coinY = random.randint(0, 720-coinSize)
								boost[1] = False
							

						#движения	
						charX += charSpeedX
						charY += charSpeedY
						
						for i in range(len(check)):
							shootX[i] += shootSpeedX[i]
							shootY[i] += shootSpeedY[i]
	
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								pygame.quit()
		
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_s:
									charSpeedY = charSpeed
								if event.key == pygame.K_w:
									charSpeedY = -charSpeed
								if event.key == pygame.K_d:
									charSpeedX = charSpeed
								if event.key == pygame.K_a:
									charSpeedX = -charSpeed
								
								
								if shootSpeedX[j] == 0 and shootSpeedY[j] == 0:		
									if event.key == pygame.K_UP:
										check[j] = False
										shootSpeedY[j] = -shootSpeed
									if event.key == pygame.K_DOWN:
										check[j] = False
										shootSpeedY[j] = shootSpeed
									if event.key == pygame.K_LEFT:
										check[j] = False
										shootSpeedX[j] = -shootSpeed
									if event.key == pygame.K_RIGHT:
										check[j] = False
										shootSpeedX[j] = shootSpeed
									j += 1
									if j > len(check)-1:
										j = 0
								else:
									j = 0

							if event.type == pygame.KEYUP:
								if event.key == pygame.K_s:
									charSpeedY = 0
								if event.key == pygame.K_w:
									charSpeedY = 0
								if event.key == pygame.K_d:
									charSpeedX = 0
								if event.key == pygame.K_a:
									charSpeedX = 0
				elif opt == 2:
					markY = 265
					markX = easyX-35
					opt = 1
					difscreen = True
					while difscreen:
						
						
						conPrint = scon.render(str(con), True, conColor)
						screen.blit(backgr, (0,0))
						screen.blit(easy, (easyX, easyY))
						screen.blit(medium, (mediumX, mediumY))
						screen.blit(hard, (hardX, hardY))
						screen.blit(count, (countX, countY))
						screen.blit(conPrint, (countX+90, countY+10))
						
						pygame.draw.circle(screen, col4, [markX, markY], 25)
						pygame.display.flip()
						
						
						

						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								pygame.quit()
			 
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_DOWN and opt < 4:
									opt += 1
									markY += 120
								if event.key == pygame.K_UP and opt > 1:
									opt -= 1
									markY -= 120
									
								if opt == 1: markX = easyX-35
								elif opt == 2: markX = mediumX-35
								elif opt == 3: markX = hardX-35	
								elif opt == 4: markX = countX-35
									
								if event.key == pygame.K_RETURN:
									difscreen = False					
									if opt == 1:
										enemySize = 80
										enemySpeed = 0
										dif = 1
										b = 0
										b2 = 2
									elif opt == 2:
										enemySize = 60
										enemySpeed = 0.2
										dif = 2
										b = 3
										b2 = 5
									elif opt == 3:
										enemySize = 40
										enemySpeed = 0.5
										dif = 3
										b = 6
										b2 = 8
									elif opt == 4:
										opt = 1
										difscreen = True
									opt = 1
									markY = 265	
									markX = startX-35
								
								if opt == 4:
									if event.key == pygame.K_RIGHT:
										con += 1
									elif event.key == pygame.K_LEFT and con > 0:
										con -= 1
									
				elif opt == 3:
					pygame.quit()
