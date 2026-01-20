import pygame as pg
from figura_class import Raqueta,Pelota

#Iniciamos todos los modulos para la pantalla
pg.init()

#raqueta izquierda
raqueta1 = Raqueta(20,300)

#raqueta derecha
raqueta2 = Raqueta(800,300)
#pelota
pelota = Pelota(400,300, color = (100,200,136))

pantalla_principal = pg.display.set_mode( (800,600) )
pg.display.set_caption("PONG")

game_over = True

#Todo lo que tenga que ver con la pantalla va dentro del while
while game_over:
    for eventos in pg.event.get():
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla_principal.fill( (35,78,198) )
    pg.draw.line( pantalla_principal,(255, 255, 255),(400,0),(400,600), width = 10 )

    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    pelota.dibujar(pantalla_principal)
    pg.display.flip()


pg.quit()