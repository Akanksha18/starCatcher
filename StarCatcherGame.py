#This is my first game demo in python
  
import pygame, sys, random
from pygame import *
pygame.init()
 
def game():
   #make window called screen and initialize the background,p.s.game is a variable
   
   width, height = 600, 400
   screen = pygame.display.set_mode((width,height))
   pygame.display.set_caption('My Star Catcher Game by Akanksha')
   background = pygame.image.load('bak.jpg')
   background=pygame.transform.scale(background, (width,height))
   screen.blit(background, (0,0))
   
   #load target image and player 
   
   target = pygame.image.load('smile.jpg')
   target=pygame.transform.scale(target, (20,20))
   targetpos = [20,20]
   screen.blit(target, targetpos)
   
   targetvisible = True 
   
   player = pygame.image.load('bunny.png')
   player=pygame.transform.scale(player, (40,40))  # 20 above plotting
   px,py = (width-40)/2, (height-40)/2  #because player size right now is 40
   screen.blit(player, (px, py))
   
   
   # speed of game and other variables initiated
   clock=pygame.time.Clock()
   gamespeed = 100
   #change game speed in upr waali line its random now
   movex = movey = 0
   speed=[gamespeed*random.randint(1,3), gamespeed*random.randint(1,5)]
   #put random no.z upar
   score=0
   
   
   # This is score text loading
   gamefont=pygame.font.Font(None, 30)
   scoretext=gamefont.render('Player Score:' +str(score), 2, [255,0,0]) # colour
   boxsize=scoretext.get_rect()
   scoreXpos=(width-boxsize[2])/2
   screen.blit(scoretext, [scoreXpos,20])
   
   
   # running of the game loop
   while True:
    
      #image and display updates
    
      screen.blit(background, (0,0))
      screen.blit(player, (px, py))
      scoretext=gamefont.render('Player Score:' +str(score), 2, [255,0,0])
      screen.blit(scoretext, [scoreXpos,20])
      
      
      if targetvisible == True:
	  seconds=clock.tick()/1000.0
	  targetpos[0]+=seconds*speed[0]
	  targetpos[1]+=seconds*speed[1]
	  screen.blit(target, targetpos)
      else:
	  screen.blit(target, (width-50,height-50))

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
	      
      if targetpos[0]>width or targetpos[0]<0:
	  speed[0] = -speed[0]
      
      if targetpos[1]>height or targetpos[1]<0:
	  speed[1] = -speed[1]
	  targetpos[1]+=seconds*speed[1]
#This is collision test	  
      if abs(targetpos[0]-px)<20 and abs(targetpos[1]-py)<20:
	  targetvisible=False
	  score+=10
	  targetpos=[width+100,height+100]
# pythons way of running a main routine is running an if statement

if __name__=='__main__':
    game()