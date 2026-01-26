import pygame as pg
from pongapp.figura_class import *
from pongapp.utils import *

class Partida:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode( (800,600) )
        pg.display.set_caption("PONG")
        self.tasa_refresco = pg.time.Clock()
        self.raqueta1 = Raqueta(20,ALTO//2)
        self.raqueta2 = Raqueta(ANCHO,ALTO//2)
        self.pelota = Pelota(ANCHO//2,ALTO//2,color= COLOR_PELOTA)
        #self.marcador_font = pg.font.SysFont("verdana", 30)
        #self.marcador_tiempo_font = pg.font.SysFont("arial", 40)
        self.marcador_font = pg.font.Font(FUENTE1,30)
        self.marcador_tiempo_font = pg.font.Font(FUENTE1,30)
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0
        self.quienMarco = ""
        self.temporizador = TIEMPO_JUEGO
        self.game_over = True
        self.colorFondo = COLOR_LILA
        self.contadorFotograma = 0
        self.resultado = ""


    def bucle_fotograma(self):
        self.game_over = True
        while self.game_over:
            self.valor_tasa = self.tasa_refresco.tick(TS)
            self.temporizador = self.temporizador - self.valor_tasa

            for eventos in pg.event.get():
                if eventos.type == pg.QUIT:
                    self.game_over = False

            self.finalizacion_juego()
            self.pantalla_principal.fill( self.fondo_juego() )

          
            self.quienMarco = self.pelota.mover(ANCHO, ALTO)
           
            

            self.mostrar_linea_central()               

            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            self.pelota.dibujar(self.pantalla_principal)

            self.raqueta1.mover(pg.K_w, pg.K_s)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)

            self.pelota.comprobar_choqueV2(self.raqueta1, self.raqueta2)
            self.mostrar_marcador()
            
        
            pg.display.flip()  

        pg.quit()

    def mostrar_linea_central(self):
        for i in range(0,ALTO,20):
            pg.draw.line( self.pantalla_principal,COLOR_BLANCO,(ANCHO//2, i),(ANCHO//2, i + 15), width = 10 )

    def mostrar_marcador(self):
        if self.quienMarco == "Derecho":
            self.contadorIzquierdo += 1
        elif self.quienMarco == "Izquierdo":
            self.contadorDerecho += 1
        marcador1 = self.marcador_font.render(str(self.contadorIzquierdo),True,COLOR_BLANCO)
        marcador2 = self.marcador_font.render(str(self.contadorDerecho),True,COLOR_BLANCO)
        jugador1 = self.marcador_font.render("Jugador 1",True,COLOR_ROSA_PALO)
        jugador2 = self.marcador_font.render("Jugador 2",True,COLOR_ROSA_PALO)
        tiempo_juego = self.marcador_tiempo_font.render(f"{int(self.temporizador/1000)}",True,COLOR_AZUL)
        self.pantalla_principal.blit(marcador1,((ALTO//2)+ 20, 60))
        self.pantalla_principal.blit(marcador2, ((ANCHO//2) + 50, 60))
        self.pantalla_principal.blit(jugador1, ((ALTO//2) - 100, 10))
        self.pantalla_principal.blit(jugador2, ((ALTO//2) + 140, 10))
        self.pantalla_principal.blit(tiempo_juego,(ANCHO//2, 50))

        

    def finalizacion_juego(self):
        #Finalización de juego por tiempo
        if self.temporizador <= 0:
            self.game_over = False
            if self.contadorIzquierdo > self.contadorDerecho:
                self.resultado = f"Jugador 1 - Resultado: Jugador1 : {self.contadorIzquierdo}, Jugador2: {self.contadorDerecho}"
            elif self.contadorDerecho >  self.contadorIzquierdo:
                self.resultado = f"Jugador 2 - Resultado: Jugador1 : {self.contadorIzquierdo}, Jugador2: {self.contadorDerecho}"
            else:
                self.resultado = f"EMPATADOS! - Resultado: Jugador1 : {self.contadorDerecho}, Jugador2: {self.contadorIzquierdo}"

            return self.resultado
        #Finalización de juego por puntaje
        if self.contadorIzquierdo == 7:
            self.game_over = False
            self.resultado = f"Jugador 1 - Resultado: Jugador1 : {self.contadorIzquierdo}, Jugador2: {self.contadorIzquierdo}"
            return self.resultado
        if self.contadorDerecho == 7:
            self.game_over = False
            self.resultado = f"Jugador 2 - Resultado: Jugador1 : {self.contadorIzquierdo}, Jugador2: {self.contadorDerecho}"
            return self.resultado


        

    def fondo_juego(self):
        self.contadorFotograma += 1
        #LOS 10 SEGUNDOS
        if self.temporizador > 10000:
            self.contadorFotograma = 0
        elif self.temporizador > 5000:
            if self.contadorFotograma == 80:
                if self.colorFondo == COLOR_FONDO:
                    self.colorFondo = PISTA_NARAJA
                else:
                    self.colorFondo = COLOR_FONDO
                self.contadorFotograma = 0
        #LOS 5 SEGUNDOS
        else:
            if self.contadorFotograma == 80:
                if self.colorFondo == COLOR_LILA or self.colorFondo == COLOR_FONDO:
                 self.colorFondo = PISA_ROJA
            else:
                self.colorFondo = COLOR_LILA
            self.contadorFotograma = 0

        return self.colorFondo
    
class Menu:
    pg.init()
    def __init__(self):
        self.patalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Menú")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo = pg.image.load(FONDO_MENU)
        self.fuente = pg.font.Font(FUENTE1,30)
        self.sonido = pg.mixer.Sound("pongapp/songs/sonido1.mp3")

    def bucle_pantalla(self):
        game_over = True
        while game_over:
            pg.mixer.Sound.play(self.sonido)
            pg.mixer.Sound.set_volume(self.sonido,0.03)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False
               
            teclado = pg.key.get_pressed()
            if teclado[pg.K_RETURN] == True:
                pg.mixer.Sound.stop(self.sonido)
                game_over = False
                return "Partida"
            elif teclado[pg.K_r] == True:
                pg.mixer.Sound.stop(self.sonido)
                return "record"


            self.patalla_principal.blit(self.imagenFondo,(0,0))
            texto_menu = self.fuente.render("Pulsa ENTER para Empezar",True,COLOR_NEGRO)
            self.patalla_principal.blit(texto_menu,(120,ALTO // 2 - 40))
            texto_record = self.fuente.render("Pulsa r para ver records",True,COLOR_BLANCO)
            self.patalla_principal.blit(texto_record,(120,ALTO // 2 - 20))
            pg.display.flip()

        pg.quit()

class Resultado:
    def __init__(self,resultado):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Resultado")
        self.tasa_refresco = pg.time.Clock()
        self.fuente_resultado = pg.font.Font(FUENTE1,10)
        self.resultado = resultado

    def bucle_pantalla(self):
        game_over = True
        while game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False
            self.pantalla_principal.fill(COLOR_BLANCO)
            texto_resultado = self.fuente_resultado.render(f"El ganador es: {self.resultado}", True, COLOR_AZUL)
            self.pantalla_principal.blit(texto_resultado,(200,ALTO//2))
            pg.display.flip()

        pg.quit()



class Record:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Mejores Puntajes")
        self.tasa_refresco = pg.time.Clock()
        self.fuente_Record = pg.font.Font(FUENTE1,10)

    def bucle_pantalla(self):
        game_over = True
        while game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False

            self.pantalla_principal.fill(COLOR_BLANCO)
            texto = self.fuente_Record.render(f"RECORD",True, COLOR_PELOTA)
            self.pantalla_principal.blit(texto,(ANCHO // 2,ALTO // 2))

            pg.display.flip()

        pg.quit()

