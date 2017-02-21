#from queue import *
from random import *

ciclo_total = 120
semaforo = {1:"Norte",2:"Sur",3:"Este",4:"Oeste"}

def car_fill():
    North = randint(2,5)
    South = randint(2,5)
    East = randint(2,5)
    West = randint(2,5)

class TrafficLight(object):

    def __init__(self):
        semaforo = {1:"Norte",2:"Sur",3:"Este",4:"Oeste"}

    def light_change(self):
        state_change = {'green':'Verde','yellow':'Amarillo','red':'Rojo'}
        for count_down in range(ciclo_total, 0, -1):
            if count_down <= 120 and count_down > 62:
                print[state_change['green'], count_down]
            if count_down <= 62 and count_down > 58:
                print[state_change['yellow'], count_down]
            if count_down <= 58:
                print[state_change['red'], count_down]

def main():
    car_fill()
    semaforo_prueba = TrafficLight()
    semaforo_prueba.light_change()

main()
