import pygame as pg
pg.init()
screen = pg.display.set_mode((1360,768),pg.FULLSCREEN)#(100, 100))
clock = pg.time.Clock()
presionado = False
c = 0
puntos = 100
black = (0, 0, 0)
w=(255, 255, 255)
arribaDerecha = pg.image.load("1.png")
arribaIzquierda = pg.image.load("3.png")
abajoDerecha = pg.image.load("0.png")
abajoIzquierda = pg.image.load("2.png")
golpeDerecha = pg.image.load("Golpe0.png")
golpeIzquierda = pg.image.load("Golpe2.png")
enemigo = pg.image.load("enemigo.png")
imagenFondo = pg.image.load("fondo.png")
miraDerecha = False
botonIzquierdoPresionado = False
botonDerechoPresionado = False
bordeIzquierda = False
bordeDerecha = False
avanzaIzquierda = False
avanzaDerecha = False
x = 100
y = 600
x_fondo = 0
Golpe = False
r = 500
x1 = 50
y1 = 600
while True:


    if x_fondo == 0 and x <= 665:
        bordeIzquierda = True
    else:
        bordeIzquierda = False
    if x_fondo <= -9310 and x >= 665:
        bordeDerecha = True
    else:
        bordeDerecha = False
    screen.blit(imagenFondo,(x_fondo,0))
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                Golpe = True
                if x-x1 > -100 or x-x1 < 100:
                    r-=100
        
    
            if event.key == pg.K_ESCAPE:
                pg.quit()
                break
            if event.key == pg.K_RIGHT:
                botonDerechoPresionado = True
                miraDerecha = True
                avanzaDerecha = True
            if event.key == pg.K_LEFT:
                botonIzquierdoPresionado = True
                miraDerecha = False
                avanzaIzquierda = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_q:
                Golpe = False
            if event.key == pg.K_RIGHT:
                botonDerechoPresionado = False
                avanzaDerecha = False
            if event.key == pg.K_LEFT:
                botonIzquierdoPresionado = False
                avanzaIzquierda = False
    if Golpe:
##        if x-x1 > -100 or x-x1 < 100:
##            r-=100
##        
##    
        if miraDerecha:        
            screen.blit(golpeDerecha,(x,y))
            
        else:
            screen.blit(golpeIzquierda,(x,y))
        
            
    if r == 0:
        print("ganaste")
        pg.quit()
               
    if avanzaDerecha and avanzaIzquierda:
        avanzaIzquierda = False
        avanzaDerecha = False
    
    if miraDerecha and not Golpe:
        if botonDerechoPresionado:
            if bordeDerecha and x<=1280:
                x+=5
            if bordeIzquierda:
                x+=5
            elif not bordeDerecha:
                x_fondo -= 5
            c+=1
            if c % 6 < 3:
                screen.blit(arribaDerecha,(x,y))
            else:
                screen.blit(abajoDerecha,(x,y))
        else:
            screen.blit(abajoDerecha,(x,y))
            c = 0
    elif not Golpe:
        if botonIzquierdoPresionado and not Golpe:
            if bordeDerecha:
                x-=5
            elif not bordeIzquierda:
                x_fondo += 5                
            if bordeIzquierda and x >= 0:
                x-=5
            c+=1
            if c % 6 < 3:
                screen.blit(arribaIzquierda,(x,y))
            else:
                screen.blit(abajoIzquierda,(x,y))
        else:
            screen.blit(abajoIzquierda,(x,y))
            c = 0

    screen.blit(enemigo, (x1,y1))
    pg.display.update()
    clock.tick(30)
