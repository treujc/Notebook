class Point:
    def __init__(self,x=0,y=0):
        """Creates a new point at (x,y)."""
        self.x = x
        self.y = y

    def info(self):
        return('Point is ({},{})'.format(self.x,self.y))

    def distance(self,other = None):
        if other == None:
            other = Point()
        d = (((self.x - other.x) ** 2) + ((self.y - other.y) ** 2)) ** .5
        return(d)
        #return('The distance between ({},{}) and ({},{}) is {:.2f} units.'.format(self.x,self.y,other.x,other.y,d))

    def distance_from_origin(self):
        dfo = self.distance()
        return(dfo)
        #return('The point ({},{}) is {:.2f} units from the origin.'.format(self.x,self.y,dfo))

    def midpoint(self,other):
        mpx = (self.x + other.x)/2
        mpy = (self.y + other.y)/2
        return('The midpoint between ({},{}) and ({},{}) is ({},{}).'.format(self.x,self.y,other.x,other.y,mpx,mpy))

    def __add__(self,other):
        return('The vector summation of ({},{}) and ({},{}) yields ({},{}).'.format(self.x,self.y,other.x,other.y,self.x+other.x,self.y+other.y))

    def line_equation(self,other):
        m = ((other.y-self.y)/(other.x-self.x))
        b = (m*(-1)*self.x)+self.y
        return('The slope-intercept equation of the line through ({},{}) and ({},{}) is: (y = {}x + {}).'.format(self.x,self.y,other.x,other.y,m,b))

if __name__ == "__main__":
    p1 = Point(1,2)
    p2 = Point(3,5)

    #print(p1.info())
    #print(p1.distance_from_origin())
    #print(p1+p2)
    print(p1.midpoint(p2))
    #print(p1.line_equation(p2))
    #print(p1.distance(p2))
    #print(p1.distance())
