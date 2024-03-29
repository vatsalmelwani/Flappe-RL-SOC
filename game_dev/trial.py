import pygame as pg
import sys
import random
import numpy as np

def obstacle_render(obs_list,obst_list):
    if obs_list:
        for i in range (len(obs_list)):
            screen.blit(pipe,pipe.get_rect(topleft=obs_list[i]))
            screen.blit(pipet,pipet.get_rect(topleft=obst_list[i]))
            obst_list[i][0]=obst_list[i][0]-4
            obs_list[i][0]=obst_list[i][0]-4
        if obs_list[0][0]<-150:
            del obs_list[0]
            del obst_list[0]
        return obs_list,obst_list
    else:
        return[],[]
        

Q_value=np.zeros((605,777,51,69),dtype=np.int32)
def out_Q_valuee(Q,state):
    return Q_valule[state[0]][state[1]+301][state[2]-150][state[3]+47]

pg.init()
screen=pg.display.set_mode((1200,576))
pg.display.set_caption("Hello")
clock=pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 22)
sky=pg.image.load('finalbg.jpg').convert()
pipe=pg.image.load('pipe.png').convert_alpha()
pipe=pg.transform.scale(pipe,(100,500))
pipet=pg.transform.rotate(pipe,180)
pipet=pg.transform.flip(pipet,True,False)
pipet_rect=pipet.get_rect(topleft=(1200,-50))
pipe_rect=pipe.get_rect(topleft=(1200,300))
pipe_rect_copy=pipe.get_rect(topleft=(550,300))
pipet_rect_copy=pipet.get_rect(topleft=(550,-50))
bird=pg.image.load('bird.png').convert_alpha()
bird=pg.transform.scale(bird,(70,50))
bird_rect=bird.get_rect(center=(124,125))
sbt=font.render("START",True,"red")
sbt_rect=sbt.get_rect(center=(600,288))
screen.blit(sbt,sbt_rect)

#defining timer for the obstacles to occur
timer=pg.USEREVENT+1
pg.time.set_timer(timer,2000)

#bird=pg.transform.rotate(bird,-30)
obs_list=[[700,400],[1100,500]]
obst_list=[[700,-300],[1100,-300]]
t=0
a=0
score="0"
#bird_rect.top=0
s=bird_rect.centery
print(s)
bird_rect.bottom=576
print(bird_rect.centery)
x1=random.randint(-250,0)
x2=random.randint(-300,-50)
text = font.render(score, True, (77,208,225))
text_rect = text.get_rect(center=(600,80))
l=[]
el=pg.draw.circle(screen,"blue",bird_rect.center,20)


while True:
    #draw everything and update
    for event in pg.event.get():
        if event.type==pg.QUIT:
            print(l)
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            s=s+t*t-t*a
            a=21
            t=0
            print("dfef")
        if event.type==timer:
            x=4*random.randint(250,300)
            y=400+random.randint(-150,100)
            obs_list.append([x,y])
            obst_list.append([x,y-700+random.randint(0,50)])
            distance=((pipe.get_rect(topleft=obs_list[1])).left-(pipe.get_rect(topleft=obs_list[0])).left)
            print(distance)
            l.append(distance)
    # defining thr rectangle postions
    el=pg.draw.circle(screen,"blue",bird_rect.center,20)
    
    #displaying the final position on the surface
    screen.blit(sky,(-100,0))
    bird_rect.centery=s+t*t-t*a
    v=a-t*2
    print(v)
    screen.blit(bird,bird_rect)
    screen.blit(text,text_rect)

    obs_list,obst_list=obstacle_render(obs_list,obst_list)

    if obs_list and el.right==obs_list[0][0]+160:
        score=str(eval(score)+1)
        text = font.render(score, True,(77,208,225))
    #if (obs_list and obst_list and (el.colliderect(pipe.get_rect(topleft=obs_list[0])) or el.colliderect(pipet.get_rect(topleft=obst_list[0])))) or bird_rect.bottom>=576 or bird_rect.top<=0:
    #    pg.quit()
    #    sys.exit()
    t=t+0.6
    pg.display.update()
    clock.tick(60) 
    #if bird_rect.y>=551:
            #s=s+t*t-t*a
            #a=21
            #t=0
    
