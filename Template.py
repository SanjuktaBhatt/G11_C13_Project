import pygame
pygame.init()
#Create the function here

  




screen = pygame.display.set_mode((300,400))
pygame.display.set_caption("Project C13")

carryOn = True
while carryOn:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False 
  screen.fill((36,90,190))
  create_building(400,100,100,255,0,0,4)
  
    
  pygame.display.flip()
    
pygame.quit()
