#!/usr/bin/env python
"""
A generic template
"""

class Fruit:
    """
    A base class fruit
    """

    def __init__(self,n_fruit):
        """
        Constructor
        """

        self.n_fruit = n_fruit
        self.l = []

    def count_fruit(self):
        return(self.n_fruit*100)

    def __str__(self):
        return("Num fruit: %s"%self.n_fruit)

    def __add__(self,other,other2=None):
        return(self.n_fruit+other.n_fruit)

class Apple(Fruit):
    """
    An apple class based on the Fruit class
    """

    def __init__(self, n_fruit, colors=None):
        if colors and not isinstance(colors,list):
            raise Exception('Invalid type for colors')
        Fruit.__init__(self,n_fruit)
        self.colors = colors

if __name__ == "__main__":

    #fruit1 = Fruit(4)
    #fruit2 = Fruit(6)
    #print(fruit1.count_fruit())

    ## demonstrate magic functions
    #print("combined", fruit1+fruit2)
    myapple = Apple(3,['red','green','yellow'])
    myapple2 = Apple(4,['green'])
    #print(myapple.colors[1])
    #print(myapple2.count_fruit())
    print("combined", myapple+myapple2)
