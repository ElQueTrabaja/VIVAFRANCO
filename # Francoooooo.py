# ¡Crea tu propio juego de disparos!

from pygame import *
from random import *
font.init()
font1 = font.SysFont(None, 36)

alto = 500
ancho = 700
window = display.set_mode((ancho, alto))
display.set_caption("Mata a @Ralong_ramdom")
#background = transform.scale(image.load("galaxy.jpg"), (ancho, alto))
window.fill((225, 220, 200))

clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(60)
    display.update()