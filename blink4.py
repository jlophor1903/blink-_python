import pygame as pg 
from timer_event import TimerEvent
import time

contador = 1
funcionando = True      #esta variable la vamos a usar para parar pygame cuando terminemos
estado = False        #esta variable es para ir cambiando el color del circulo.
color = [(220,220,0), (50,50,50)]
pg.init()
screen = pg.display.set_mode((500,500),0 ,32 )

def blink(packet):
    global estado
    estado = not(estado)

te = TimerEvent(interval=1.0) 
te.subscribe("Temporizador1_handler" , blink) 

while funcionando:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            funcionando = False
            break
  
        estado = not(estado)
    
    screen.fill([100, 100, 100])  
    
    pg.draw.circle(screen, color[estado] ,(200,200), 70) 
    pg.display.flip()
te.stop()
pg.quit()
exit()