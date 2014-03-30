#This is my first game demo in python
  
import pygame, sys, random
from pygame import *
pygame.init()
 
def game():
   #make window called screen and initialize the background,p.s.game is a variable
   
   width, height = 800, 750
   screen = pygame.display.set_mode((width,height))
   pygame.display.set_caption('My Star Catcher Game by Akanksha')
   background = pygame.image.load('bak.jpg')
   background=pygame.transform.scale(background, (width,height))

   
   #load target in array and load player site
   playerwidth, playerheigth = 40, 40
   targetwidth, targetheigth = 20, 20
   targetnum=10  # no of targets
   target=[]
   for i in range(targetnum):
	 targetimage = pygame.image.load('smile.jpg')
	 targetimage=pygame.transform.scale(targetimage, (20,20))
	 target.append([])
	 target[i]=targetimage
	 
   targetpos=[]
   targetspace=height/targetnum-40/2
   for i in range(targetnum):
	 targetpos.append([])
	 for j in range(2):
	      targetpos[i].append(i*j*targetspace+targetwidth)
    
   # targetvisible set up of the array
   targetvisible=[]
   for i in range(targetnum):
	targetvisible.append(True)
	
   
   
   #load the player image
   player = pygame.image.load('bunny.png')
   player=pygame.transform.scale(player, (playerwidth,playerheigth))  # 20 above plotting
   px,py = (width-40)/2, (height-40)/2  #because player size right now is 40
  
   
   
   # speed of game and other variables initiated
   clock=pygame.time.Clock()
   gamespeed = 200    #change game speed in upr waali line its random now
   movex = movey = 0
   
   speed=[]
   for i in range(targetnum):
	speed.append([])
	for j in range(2):
	    speed[i].append(gamespeed*random.randint(1,5))
	    
   score=0
   
   
   # This is score text loading
   gamefont=pygame.font.Font(None, 30)
   scoretext=gamefont.render('Player Score:' +str(score), 2, [255,0,0]) # colour
   boxsize=scoretext.get_rect()
   scoreXpos=(width-boxsize[2])/2
   
   startscreen=True
   while startscreen:
	    screen.blit(background, (0,0))
	    screen.blit(player, (px,py))
	    scoretext=gamefont.render('Player Score:' +str(score), 2, [255,0,0])
	    screen.blit(scoretext, [scoreXpos,20])
	    for i in range(targetnum):
		targetimage=target[i]
		x=targetpos[i][0]
		y=targetpos[i][1]
		screen.blit(targetimage, (x,y))
	    instructtext=gamefont.render('Use the keyboard to collect the stars',1,[255,0,200])
	    screen.blit(instructtext, [targetwidth*3,60])
	    instructtext2=gamefont.render('Use the space bar to start to collect the stars',1,[255,0,255])
	    screen.blit(instructtext2, [targetwidth*3,160])
	    pygame.display.update()
	    for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    pygame.quit()
	      	elif event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_SPACE:
			startscreen=False
   
   
   # running of the game loop
   while True:
    
      #image and display updates
      seconds=clock.tick()/1000.0
      screen.blit(background, (0,0))
      screen.blit(player, (px, py))
      scoretext=gamefont.render('Player Score:' +str(score), 2, [255,0,0])
      screen.blit(scoretext, [scoreXpos,20])
      
      #  targets blitted through a for loop
      for i in range(targetnum):
	  if targetvisible[i]:
	      targetpos[i][0]+=seconds*speed[i][0]
	      targetpos[i][1]+=seconds*speed[i][1]
	      targetimage=target[i]
	      x=targetpos[i][0]
	      y=targetpos[i][1]
	      screen.blit(targetimage, (x,y))
	  else:
	      targetimage=target[i]
	      x=width-50
	      y=height-(i+1)*targetspace

      pygame.display.update()
        
        
      #keyboard or mouse movements
      for event in pygame.event.get():
	  if event.type == pygame.QUIT:
	      pygame.quit()
	      
	  elif event.type == pygame.KEYDOWN:
	      if event.key == pygame.K_RIGHT:
		#k for keyboard
		  movex = 2
	      if event.key == pygame.K_LEFT:
		  movex = -2
		    
	      if event.key == pygame.K_UP:
		  movey = -2
		
	      if event.key == pygame.K_DOWN:
		  movey = 2
		
	  
	  elif event.type == pygame.KEYUP: #when u release the key it is called keyup
	      if event.key == pygame.K_RIGHT:
		  movex = 0
	      if event.key == pygame.K_LEFT:
		  movex = 0
		    
	      if event.key == pygame.K_UP:
		  movey = 0
		
	      if event.key == pygame.K_DOWN:
		  movey = 0
		
      px = px + movex
      py = py + movey
	
      # test for the sides of the screen
      for i in range(targetnum):
	  if targetpos[i][0]>width or targetpos[i][0]<0:
	      speed[i][0] = -speed[i][0]
	  
	  if targetpos[i][1]>height or targetpos[i][1]<0:
	      speed[i][1] = -speed[i][1]
	      targetpos[i][1]+=seconds*speed[i][1]
#This is collision test	  
      for i in range(targetnum):
	  if abs(targetpos[i][0]-px)<20 and abs(targetpos[i][1]-py)<20:
	      targetvisible[i]=False
	      score+=10
	      targetpos[i]=[width+100,height+100]
	      
      # loop background
      if score ==targetnum*10:
	  pygame.time.display(2000)
	  game()
      
      
# pythons way of running a main routine is running an if statement

if __name__=='__main__':
    game()