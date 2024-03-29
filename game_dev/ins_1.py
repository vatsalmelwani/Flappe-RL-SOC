import pygame as pg
import sys
import random

def obstacle_render(obs_list):
    if obs_list:
        for obs in obs_list:
            screen.blit(pipe,obs)
            screen.blit(pipet,(obs.x,obs.y+random.randint(10,50)-250))
        if obs_list[0].x<-100:
            del obs_list[0]

pg.init()
screen=pg.display.set_mode((1200,576))
pg.display.set_caption("Hello")
clock=pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 22)
sky=pg.image.load('finalbg.jpg').convert()
pipe=pg.image.load('pipe.png').convert_alpha()
pipe=pg.transform.scale(pipe,(160,500))
pipet=pg.transform.rotate(pipe,180)
pipet=pg.transform.flip(pipet,True,False)
pipet_rect=pipet.get_rect(topleft=(1200,-50))
pipe_rect=pipe.get_rect(topleft=(1200,300))
pipe_rect_copy=pipe.get_rect(topleft=(550,300))
pipet_rect_copy=pipet.get_rect(topleft=(550,-50))
bird=pg.image.load('bird.png').convert_alpha()
bird=pg.transform.scale(bird,(70,50))
bird_rect=bird.get_rect(center=(102,100))
sbt=font.render("START",True,"red")
sbt_rect=sbt.get_rect(center=(600,288))
screen.blit(sbt,sbt_rect)

#defining timer for the obstacles to occur
timer=pg.USEREVENT+1
pg.time.set_timer(timer,2000)

#bird=pg.transform.rotate(bird,-30)
obs_list=[]
t=0
t1=t2=0
u=0
a=0
score="0"
y11=y21=y12=y22=0
s=100
x1=random.randint(-250,0)
x2=random.randint(-300,-50)
text = font.render(score, True, (77,208,225))
text_rect = text.get_rect(center=(600,80))
while True:
    #draw everything and update
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            s=s+t*t*1.5-t*a
            a=25
            t=0
        if event.type==timer:
            obs_list.append(4*random.randint(300,375),300 + random.randint(-200,100))
    # defining thr rectangle postions
    pipe_rect.topleft=(1200-t1,500+x1-y21)
    pipet_rect.topleft=(1200-t1,-250+x1+y11)
    pipe_rect_copy.topleft=(552-t2,550+x2-y22)
    pipet_rect_copy.topleft=(552-t2,-200+x2+y12)
    bird_rect.centery=s+t*t*1.5-t*a
    el=pg.draw.circle(screen,"blue",bird_rect.center,18)
    
    #displaying the final position on the surface
    screen.blit(sky,(-100,0))
    screen.blit(pipe,pipe_rect)
    screen.blit(pipet,pipet_rect)
    screen.blit(pipe,pipe_rect_copy)
    screen.blit(pipet,pipet_rect_copy)
    screen.blit(bird,bird_rect)
    screen.blit(text,text_rect)
    
    if pipe_rect.centerx<=-96:
        t1=0
        x1=random.randint(-250,0)
        y11=random.randint(20,60)
        y21=random.randint(20,60)
    if pipe_rect_copy.centerx<=-96:
        t2=-648
        x2=random.randint(-250,0)
        y12=random.randint(20,60)
        y22=random.randint(20,60)
    if el.right==pipe_rect_copy.right or el.right==pipe_rect.right:
        score=str(eval(score)+1)
        text = font.render(score, True,(77,208,225))
    if pipe_rect.colliderect(el) or pipet_rect.colliderect(el) or pipe_rect_copy.colliderect(el) or pipet_rect_copy.colliderect(el):
        pg.quit()
        sys.exit()
    t=t+0.4
    t1=t1+4
    t2=t2+4
    pg.display.update()
    clock.tick(60)   #does not let the frame rate to be higher than 60