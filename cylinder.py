import math
class cylinder:
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
    
    def volume(self):
        r=self.radius
        h=self.height
        volume=math.pi*r*r*h
        return volume
    def surface_are(self):
        r=self.radius
        h=self.height
        surf_area=2*math.pi*r*(r+h)
        return surf_area
c=cylinder(2,3)
print("Volume is : ",end=' ')
print(round(c.volume(),2))
print("Surface area is : ",end=' ')
print(round(c.surface_are(),1))
