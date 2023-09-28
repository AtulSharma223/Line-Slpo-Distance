import math
class Line:
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    def distance(self):
        x1=self.coor1[0]
        y1=self.coor1[1]

        x2=self.coor2[0]
        y2=self.coor2[1]

        dist=math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
        return dist

    def slop(self):
        x1=self.coor1[0]
        y1=self.coor1[1]

        x2=self.coor2[0]
        y2=self.coor2[1]

        slop=(y2-y1)/(x2-x1)

        return slop
    
coordinate1=(3,2)
coordinate2=(8,10)
li=Line(coordinate1,coordinate2)
print("Distance between two points is : ",end=' ')
print(li.distance())
print("Slop of line is : ",end=' ')
print(li.slop())
