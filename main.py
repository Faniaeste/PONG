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
#Definir tiempo de tasa de refreso dentro del bucle de fotogramas, fps = fotograma por segundo
tasa_refresco = pg.time.Clock()

#Agregar texto a marcadores
#Asignación de fuente y tamaño de letra
marcador1_font = pg.font.SysFont("verdana", 30)
marcador2_font = pg.font.SysFont("verdana", 30)




game_over = True

#Todo lo que tenga que ver con la pantalla va dentro del while
while game_over:
    #obtenemos la tasa de resfresco en milisegundos
    valor_tasa = tasa_refresco.tick(400)#Variable para controlar la velocidad entre fotogramas
    #print(valor_tasa)
    for eventos in pg.event.get():
        if eventos.type == pg.QUIT:
            game_over = False

    
    pelota.mover(800,600)

    pantalla_principal.fill( (35,78,198) )
    """
        #pg.draw.line( pantalla_principal,(255, 255, 255),(400,0),(400,600), width = 10 )

    
    raya = 15
    espacio = 10
    y = 0
    #while y < 600:
     #   pg.draw.line( pantalla_principal,(255, 255, 255),(x,y),(x, y + raya ), width = 10 )
      #  y += raya + espacio
      """
    

    x = 400
    for i in range(0, 600, 20):
        pg.draw.line( pantalla_principal,(255, 255, 255),(x,i),(x,i + 15), width = 10 )

    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    pelota.dibujar(pantalla_principal)

    raqueta1.mover(pg.K_w,pg.K_s)
    raqueta2.mover(pg.K_UP,pg.K_DOWN)
    print(pelota.contadorIzquierdo)
    print(pelota.contadorDerecho)
    #Asiganción de color y texto
    marcador1 = marcador1_font.render("10", True,(255, 255, 255))
    marcador2 = marcador2_font.render("10", True,(255, 255, 255))
    pantalla_principal.blit(marcador1,(310,50))
    pantalla_principal.blit(marcador2, (450,50))
    
    pg.display.flip()


pg.quit()