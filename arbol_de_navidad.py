#!/usr/bin/env python
# Christmas Tree

class ChristmasTree(object):

    def __init__(self):
        height = 0

    def height_input(self):
        global height
        height = input('Please type the hegiht of the tree: ')

    def radius_calc(self):
        global radius
        radius = 0.43125*height

    def height_per_level(self):
        global height_pl, diameter
        if height >= 0.1 and height < 1:
            height_pl = 0.08
            diameter = .03
        if height >= 1 and height < 2.24:
            height_pl = 0.15
            diameter = .06
        if height >= 2.25 and height < 5:
            height_pl = 0.25
            diameter = .12
        if height >= 5:
            height_pl = 0.40
            diameter = .18

    def number_of_levels(self):
        global level_number
        level_number = (height/height_pl) - 1
        level_number = int(round(level_number))

    def perimeter_per_level(self):
        global perimeter, bubbles
        print ("\n==========================LINES==========================")
        for i in range(level_number):
            i += 1
            perimeter = (i*height_pl*2*radius*3.1416)
            bubbles = perimeter/diameter*.5
            bubbles += bubbles
            print("\n The perimeter of the level: %r is: %1.2f,\n and the number of bubbles to cover up this line is: %1.0f" %(i,perimeter,bubbles))
        print ("============================LINES==========================")

    def print_output(self):
        print("===========================DATA==========================")
        print(' Height: %1.2f' %(height))
        print(' Radius: %f' %(radius))
        print(' Height per level: %r' %(height_pl))
        print(' Number of levels: %r' %(level_number))
        print("===========================DATA==========================")

    def total_of_bubbles(slef):
        print("\n===========================BUBBLES==========================")
        print("\n The total of bubbles are: %1.0f" %(bubbles))
        print("\n===========================BUBBLES==========================")

def main():
    new_tree = ChristmasTree()
    new_tree.height_input()
    new_tree.radius_calc()
    new_tree.height_per_level()
    new_tree.number_of_levels()
    new_tree.print_output()
    new_tree.perimeter_per_level()
    new_tree.total_of_bubbles()

main()
