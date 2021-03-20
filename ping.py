import pygame
import numpy as np
pygame.init()
#variables
WIDTH=1200
HEIGHT=600
BORDER=20
VELOCITY=10
fgcolor=pygame.Color("white")
bgcolor=pygame.Color("black")
#colour=pygame.Color("white")

class ball:
    RADIUS=20
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
    
    def show(self,colour):
        global screen
        pygame.draw.circle(screen, colour, (self.x,self.y), self.RADIUS)
        
    def update(self):
        global bgcolor,fgcolor
        self.show(bgcolor)

        newx=self.x + self.vx
        newy= self.y +self.vy
        if newy<BORDER+self.RADIUS+1 and newx>BORDER+self.RADIUS:
            self.vy=-self.vy
            self.x=newx
            self.y=newy
            self.show(fgcolor)
        #top corner
        elif newx<BORDER+21 and newy<BORDER+21:
            self.vx=-self.vx
            self.vy=-self.vy
            self.x=newx
            self.y=newy
            self.show(fgcolor)
        #bottom corner
        elif newx<BORDER+21 and newy>HEIGHT-41:
            self.vx=-self.vx
            self.vy=-self.vy
            self.x=newx
            self.y=newy
            self.show(fgcolor)

        #leftwall which will soon be raplaced
        elif newx<BORDER+self.RADIUS+1 :
            self.vx=-self.vx
            self.x=newx
            self.y=newy
            self.show(fgcolor)

        #bottom wall
        elif newy>HEIGHT-41 and newx>BORDER:
            self.vy=-self.vy
            self.x=newx
            self.y=newy
            self.show(fgcolor)

        #collision with paddle
        elif paddleplay.main.collidepoint(newx,newy):
            self.vx=-self.vx
            self.x=newx
            self.y=newy
            self.show(fgcolor)
        
        #you lose
        elif newx>WIDTH:

            pygame.quit()

        else:
            self.x=newx
            self.y=newy
            self.show(fgcolor)
        
class paddle:
    WIDTH=20
    HEIGHT=100
    
    def __init__(self,y):
        self.y=y
    
    def show(self,colour):
        global screen
        pygame.draw.rect(screen,colour,pygame.Rect(WIDTH-self.WIDTH,self.y-self.HEIGHT//2,self.WIDTH,self.HEIGHT+100))
        self.main=pygame.Rect(WIDTH-self.WIDTH,self.y-self.HEIGHT//2,self.WIDTH,self.HEIGHT+100)
    
    def update(self):
        #print(self.y)
        self.show(bgcolor)
        #self.y=pygame.mouse.get_pos()[1]
        pda=np.array([[ballplay.x,ballplay.y,ballplay.vx,ballplay.vy]])
        #print(pda)
        #print(model.predict(pda))
        #model.predict([X.to_numpy()[0],X.to_numpy()[0]])
        self.y=int(model.predict(pda))
       	self.show(fgcolor)


ballplay = ball(WIDTH-ball.RADIUS,HEIGHT//2,-VELOCITY,-VELOCITY)
paddleplay=paddle(400)


#the screen /scenario
screen=pygame.display.set_mode((1200,600))



pygame.draw.rect(screen,pygame.Color("white"),pygame.Rect((0,0,WIDTH,BORDER)))
pygame.draw.rect(screen,pygame.Color("white"),pygame.Rect((0,0,BORDER,HEIGHT)))
pygame.draw.rect(screen,pygame.Color("white"),pygame.Rect((0,HEIGHT-BORDER,WIDTH,BORDER)))


# performing data science

import pandas as pd



ping=pd.read_csv("game1.csv")


ping=ping.drop_duplicates()


from sklearn.neighbors import KNeighborsRegressor

regressor=KNeighborsRegressor(n_neighbors=3)


X=ping.drop(columns="Paddle.y")

Y=ping["Paddle.y"]

model=regressor.fit(X,Y)


prediction=model.predict(X)




#the game

ballplay.show(fgcolor)
paddleplay.show(fgcolor)



   
clock=pygame.time.Clock()   

#sample=open("game.csv","w")
#print("x,y,vx,vy,Paddle.y",file=sample)

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    clock.tick(50)
    pygame.display.flip()
    ballplay.update()
    paddleplay.update()

    #print("{},{},{},{},{}".format(ballplay.x,ballplay.y,ballplay.vx,ballplay.vy,paddleplay.y),file=sample)

pygame.quit()
