#Ventana

import turtle
import time
import random

posponer = 0.1

#Marcador

Puntos = 0
Mejor_Puntuación = 0


wn = turtle.Screen()
wn.title("Juego de snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#Cabeza de la serpiente

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("red")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida

comida = turtle.Turtle()
comida.shape("circle")
comida.color("white")
comida.penup()
comida.goto(60,100)

#Cuerpo de la serpiente

segmentos = []

#Texto

texto = turtle.Turtle()
texto.speed(0)
texto.color("light green")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Puntos: 0        Mejor Puntuación: 0"
            , align = "center", font=("Courier", 18, "normal"))

#Funciones

def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#Teclado

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()

    #Colision borde
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(0.5)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #Esconder segmentos

        for segmento in segmentos:
            segmento.goto(1000,1000)

        #limpiar lista
        segmentos.clear()

        #Resetear puntuacion
        Puntos = 0
        texto.clear()
        texto.write("Puntos: {}     Mejor Puntuacion: {}".format(Puntos, Mejor_Puntuación),
                        align= "center", font= ("Courier",18,"normal"))
#Colision comida

    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,275)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("light blue")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #Aumentar marcador
        Puntos += 1

        if Puntos > Mejor_Puntuación:
            Mejor_Puntuación = Puntos
        texto.clear()
        texto.write("Puntos: {}          Mejor Puntuación: {}".format(Puntos, Mejor_Puntuación),
                    align = "center", font=("Courier", 18, "normal"))


    #Mover el cuerpo

    totalseg = len(segmentos)
    for index in range(totalseg -1,0,-1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x,y)

    if totalseg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()
    time.sleep(posponer)

