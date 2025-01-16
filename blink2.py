import pygame as pg 
import time

funcionando = True      #esta variable la vamos a usar para parar pygame cuando terminemos
estado = False        #esta variable es para ir cambiando el color del circulo.
color = [(220,220,0), (50,50,50)]
pg.init()
screen = pg.display.set_mode((500,500),0 ,32 )
tiempoInicial = time.process_time()*1000

while funcionando:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            funcionando = False
            break
    tiempoActual = time.process_time()*1000
    if (tiempoActual - tiempoInicial) > 500:
        """
        if estado:
            color = [200,200,0]
            estado = False
        else: 
            color =  [50,50,50]
            estado = True
            """
        tiempoInicial = time.process_time()*1000
        estado = not(estado)
    
    screen.fill([100, 100, 100])  
    pg.draw.circle(screen, color[estado] ,(200,200), 70) 
    pg.display.flip()

for i in range(10000000):
     continue 

pg.quit()   