import pygame
pygame.init()

# Define a function 'create_building'
def                (height,x,y,r,g,b,windows):
  
  # Provide values of x and y coordinates into 'Rect()' function 
  building = pygame.Rect(     ,     ,60,height)
  # Draw the 'building' object on screen
  pygame.draw.rect(screen,(r,g,b),              )
  
  # Provide width and height of the 'door' object
  door=pygame.Rect(x+15,340,       ,      )
  # Draw the 'door' object on screen
  pygame.draw.rect(           ,(0,0,0),door)
  
  # Set the upper limit of the range function to the given number of windows
  for i in range(1,            ):
    window=pygame.Rect(x+20,50*i+60,20,20)
    pygame.draw.rect(screen,(255,255,0),window)
  
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
